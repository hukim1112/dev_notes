from tensorpack.dataflow import BatchData, DataFlow, PrefetchData, TestDataSpeed
from tensorpack import imgaug, AugmentImageComponent
from tensorpack import QueueInput
from tensorpack.input_source.input_source import EnqueueThread
import tensorflow as tf
import random
import numpy as np
import os
import cv2
import multiprocessing

# reference
# https://github.com/tensorpack/tensorpack/blob/master/docs/tutorial/extend/dataflow.md
# https://github.com/tensorpack/tensorpack/blob/master/docs/tutorial/efficient-dataflow.md#ref
# https://github.com/tensorpack/tensorpack/blob/master/docs/tutorial/input-source.md
# http://openresearch.ai/t/tensorpack-multigpu/45
class my_dataset_flow(DataFlow):
    def __init__(self, image_path_list, split_name, class_names_to_ids):
        assert split_name in ['train', 'validation']
        self.image_path_list = image_path_list
        self.split_name = split_name
        self.class_names_to_ids = class_names_to_ids
    def get_data(self):
        for image_path in self.image_path_list:
            class_name = os.path.basename(os.path.dirname(image_path))
            class_id = self.class_names_to_ids[class_name]
            yield [cv2.imread(image_path), class_id]          
    def size(self):
        return len(self.image_path_list)
def _get_filenames_and_classes(dataset_dir):
      flower_root = os.path.join(dataset_dir, 'flower_photos')
      directories = []
      class_names = []
      for dir_name in os.listdir(flower_root):
        path = os.path.join(flower_root, dir_name)
        if os.path.isdir(path):
          directories.append(path)
          class_names.append(dir_name)

      photo_filenames = []
      for directory in directories:
        for filename in os.listdir(directory):
          path = os.path.join(directory, filename)
          photo_filenames.append(path)

      return photo_filenames, sorted(class_names)


path = '/home/dan/prj/datasets'
photo_filenames, class_names = _get_filenames_and_classes(path)

random.seed(0)
_NUM_VALIDATION = 350
random.shuffle(photo_filenames)
training_filenames = photo_filenames[:_NUM_VALIDATION]
validataion_filenames = photo_filenames[_NUM_VALIDATION:]
class_names_to_ids = dict(zip(class_names, range(len(class_names))))

train_dataset = my_dataset_flow(training_filenames, 'train', class_names_to_ids)

batchsize = 256
nr_prefetch = 10
nr_proc = 2

ds = AugmentImageComponent(train_dataset, [imgaug.Resize((299, 299))])
#ds = PrefetchData(ds, 1000, multiprocessing.cpu_count())
'''중요한 점은, 데이터를 읽는 부분이나 rotation, flip, crop 등의 augmentation을 정의하고 이를 PrefetchData에 넘기면 필요한 부분을 여러 프로세스로 띄워서 처리해준다는 점입니다.'''


ds = BatchData(ds, batchsize, use_list=True)
ds = PrefetchData(ds, nr_prefetch, nr_proc)

TestDataSpeed(ds).start()
j = 0
for i in ds.get_data():
   j += 1
   print(i[1][0].__class__)


placeholder = [tf.placeholder(dtype = tf.int8, shape=(None, 299, 299, 3)), 
               tf.placeholder(dtype = tf.int8, shape=(None))]
queue = tf.FIFOQueue(500, [x.dtype for x in placeholder])
thread = EnqueueThread(queue, ds, placeholder)
tensors = queue.dequeue()

sess = tf.Session()
with sess.as_default():
    thread.start()
    for i in range(100):
       imgs, labels = sess.run(tensors)
       print(imgs.shape)
       print(labels.shape)