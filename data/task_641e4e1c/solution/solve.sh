#!/bin/bash
set -e
cd /home/user

ls /home/user/migration_project/
cat /home/user/migration_project/install_spec.txt
python3 -m venv /home/user/migration_project/venv
sudo apt install -y python3-venv
python3 --version
sudo apt install -y python3.10-venv
python3 -m venv --without-pip /home/user/migration_project/venv
python3 -m ensurepip --root /home/user/migration_project/venv
curl -sS https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py && /home/user/migration_project/venv/bin/python3 /tmp/get-pip.py
wget -q https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py && /home/user/migration_project/venv/bin/python3 /tmp/get-pip.py
python3 -c "import urllib.request; urllib.request.urlretrieve('https://bootstrap.pypa.io/get-pip.py', '/tmp/get-pip.py')"
/home/user/migration_project/venv/bin/python3 /tmp/get-pip.py
/home/user/migration_project/venv/bin/pip install requests==2.28.2 boto3==1.26.90 click==8.1.3
/home/user/migration_project/venv/bin/pip freeze > /home/user/migration_project/requirements_frozen.txt
printf 'venv_path=/home/user/migration_project/venv\npackages=requests,boto3,click\n' > /home/user/migration_project/venv_info.txt
ls /home/user/migration_project/venv/bin/python && cat /home/user/migration_project/requirements_frozen.txt && echo "---" && cat /home/user/migration_project/venv_info.txt
