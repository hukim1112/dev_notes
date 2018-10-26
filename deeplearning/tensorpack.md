https://uoguelph-mlrg.github.io/getting-started/



https://github.com/tensorpack/tensorpack/issues/436



http://openresearch.ai/t/tensorpack-multigpu/45



https://github.com/tensorpack/tensorpack/blob/master/examples/basics/mnist-convnet.py





https://github.com/tensorpack/tensorpack/blob/master/docs/tutorial/efficient-dataflow.md



https://github.com/tensorpack/tensorpack/blob/master/docs/tutorial/extend/dataflow.md











# Build your efficient DataFlow

이번 튜토리얼은 python을 사용하여 어떻게 효율적인 DataFlow를 구축할 수 있는지에 대한 예시를 정리한 것이다. 우리의 목표는 **python generator**를 사용하여 image data를 preprocessing하고, 빠르게 label까지 하는 것이다. 이때 Python generator의 interface를 사용하기 때문에 Python 계열의 Deep Learning framework에서는 공통적으로 이번 튜토리얼의 코드를 활용할 수 있을 것이다.

### DataFlow란 무엇인가?

DataFlow는 데이터를 효과적으로 가져오기 위해 python iterator를 구축하는 library이다. 

DataFlow는 Python container object로, iterative한 generator method와 dataflow의 길이를 반환하는 length method로 구현되어있다.



GPU를 최대한 활용하기 위해서는 초당 1~3k 정도의 image를 가져올 수 있어야 한다.