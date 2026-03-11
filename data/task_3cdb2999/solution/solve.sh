#!/bin/bash
set -e
cd /home/user

ls /home/user/data/ /home/user/scripts/ 2>/dev/null && cat /home/user/data/sales_raw.csv 2>/dev/null && cat /home/user/scripts/clean_sales.py 2>/dev/null
python3 -m venv /home/user/envs/datawork
sudo apt install -y python3-venv python3.10-venv
python3 --version && which python3 && pip3 --version && which virtualenv 2>/dev/null || echo "no virtualenv"
python3 -m venv --without-pip /home/user/envs/datawork
/home/user/envs/datawork/bin/python3 -m ensurepip --upgrade
curl -sS https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py && /home/user/envs/datawork/bin/python3 /tmp/get-pip.py
wget -q https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py && /home/user/envs/datawork/bin/python3 /tmp/get-pip.py
/home/user/envs/datawork/bin/python3 -c "import urllib.request; urllib.request.urlretrieve('https://bootstrap.pypa.io/get-pip.py', '/tmp/get-pip.py')" && /home/user/envs/datawork/bin/python3 /tmp/get-pip.py
/home/user/envs/datawork/bin/pip install pandas==2.2.2 numpy==1.26.4
/home/user/envs/datawork/bin/python3 /home/user/scripts/clean_sales.py
cat /home/user/data/sales_clean.csv
