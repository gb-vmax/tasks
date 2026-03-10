#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/datasets_project && python3 -m venv /home/user/datasets_project/venv
sudo apt install -y python3-venv python3.10-venv
python3 --version && which python3 && pip3 --version 2>/dev/null || true
virtualenv --version 2>/dev/null || pip3 install virtualenv --user 2>&1 | tail -5
/home/user/.local/bin/virtualenv /home/user/datasets_project/venv
/home/user/datasets_project/venv/bin/pip install numpy==1.26.4 pandas==2.2.2
/home/user/datasets_project/venv/bin/pip install numpy==1.26.4 pandas==2.2.2 --timeout 300 --retries 5
/home/user/datasets_project/venv/bin/pip freeze > /home/user/datasets_project/requirements.txt
cat /home/user/datasets_project/requirements.txt
ls /home/user/datasets_project/venv/bin/pip && echo "---" && cat /home/user/datasets_project/requirements.txt
