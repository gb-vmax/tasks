#!/bin/bash
set -e
cd /home/user

python3 -m venv /home/user/profiling_env
sudo apt install -y python3.10-venv
python3 --version && apt-cache search python3.*venv
apt-cache search python | grep -i venv
pip3 install virtualenv
virtualenv /home/user/profiling_env
/home/user/profiling_env/bin/pip install pyinstrument==4.6.1 memory-profiler==0.61.0
/home/user/profiling_env/bin/pip freeze > /home/user/profiling_env/requirements.txt
cat /home/user/profiling_env/requirements.txt
