#!/bin/bash
set -e
cd /home/user

ls /home/user/automation_project/
cat /home/user/automation_project/run_workflow.py
python3 -m venv /home/user/automation_project/venv
sudo apt install -y python3.10-venv
python3 --version && which python3
sudo apt-get install -y python3-venv
pip3 install virtualenv 2>/dev/null || sudo pip3 install virtualenv
virtualenv /home/user/automation_project/venv
/home/user/automation_project/venv/bin/pip install requests==2.28.2 schedule==1.2.0 python-dotenv==1.0.0
/home/user/automation_project/venv/bin/pip freeze > /home/user/automation_project/requirements.txt
/home/user/automation_project/venv/bin/python /home/user/automation_project/run_workflow.py
cat /home/user/automation_project/requirements.txt
