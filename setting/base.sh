sudo apt-get update
sudo apt-get upgrade

sudo ln -sfn /usr/bin/python3.6 /usr/bin/python
# change the default python version into 3.6

sudo apt-get install python3-dev
sudo apt-get install python3-pip

cat >>.bashrc<<EOF
export LC_ALL=C
EOF


sudo apt install mkvirtualenvwrapper

# ~16.04
cat >>$HOME/.bashrc<<EOF
export WORKON_HOME=~/.virtualenvs
. /usr/local/bin/virtualenvwrapper.sh
EOF

# ~18.04
cat >>$HOME/.bashrc<<EOF
export WORKON_HOME=~/.virtualenvs
. $HOME/.local/bin/virtualenvwrapper.sh
EOF

source ~/.bashrc

mkvirtualenv envname --python=python3

workon envname

pip3 install ipython
pip3 install --upgrade --force-reinstall --no-cache-dir jupyter
pip3 install ipykernel

python -m ipykernel install --user --name=envname