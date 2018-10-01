if [${1} -n ] ; then
	echo 'use like this : bash virsualenv.sh my_virtualenv_name'
	exit 1
else
	echo 'make envname :' ${1}
fi

mkdir .virtualenvs
sudo pip install virtualenv virtualenvwrapper
echo "=================================================================="

if grep -q virtualenvwrapper ~/.bashrc; then
	echo 'already virtualenvwrapper.sh was registered'
else
	echo 'register virtualenvwrapper.sh'
cat >>$HOME/.bashrc<<EOF
export WORKON_HOME=~/.virtualenvs
. /usr/local/bin/virtualenvwrapper.sh
EOF
fi

source ~/.bashrc

if [ ! -d $HOME/.virtualenvs/${1} ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
echo ${1} 'will be created'
source `which virtualenvwrapper.sh`
mkvirtualenv ${1} --python=python3
pip install ipykernel
pip install ipython
pip install jupyter
python -m ipykernel install --user --name=${1}
else
	echo 'already envname exists : ' ${1}
fi

