sudo apt-get update
sudo apt-get upgrade

sudo ln -sfn /usr/bin/python3.6 /usr/bin/python
# if you want to change the default python version into 3.6

sudo apt-get install python3-dev
sudo apt-get install python3-pip

cat >>.bashrc<<EOF
export LC_ALL=C
EOF

sudo pip3 install virtualenv virtualenvwrapper

# ~18.04, set the path to virtualenv program and python3
cat >>$HOME/.bashrc<<EOF
export WORKON_HOME=~/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source /usr/local/bin/virtualenvwrapper.sh
EOF

source ~/.bashrc

mkvirtualenv envname --python=python3

workon envname

pip3 install ipython
pip3 install --upgrade --force-reinstall --no-cache-dir jupyter
pip3 install ipykernel

python -m ipykernel install --user --name=envname
