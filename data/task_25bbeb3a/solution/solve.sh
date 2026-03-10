#!/bin/bash
set -e
cd /home/user

ls /home/user/research/
cat /home/user/research/requirements.txt
cat /home/user/research/check_env.py
python3 -m venv /home/user/research/venv
sudo apt install -y python3.10-venv
python3 --version && which python3
sudo apt-get update && sudo apt-get install -y python3-venv
python3 -m venv /home/user/research/venv
/home/user/research/venv/bin/pip install -r /home/user/research/requirements.txt
sudo chown -R user:user /home/user/.cache && /home/user/research/venv/bin/pip install --no-cache-dir -r /home/user/research/requirements.txt
mkdir -p /home/user/.cache && /home/user/research/venv/bin/pip install --no-cache-dir -r /home/user/research/requirements.txt
/home/user/research/venv/bin/python /home/user/research/check_env.py
cat /home/user/research/env_status.txt
