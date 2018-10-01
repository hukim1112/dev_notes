sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-dev
sudo apt-get install python-pip

cat >>.bashrc<<EOF
export LC_ALL=C
EOF
source ~/.bashrc