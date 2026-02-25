#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/user_management
python3 -m venv /home/user/user_management/venv
sudo apt-get update && sudo apt-get install -y python3-venv
python3 -m venv /home/user/user_management/venv
ls -1 /home/user/user_management | sort > /home/user/user_management/setup_log.txt
cat /home/user/user_management/setup_log.txt
