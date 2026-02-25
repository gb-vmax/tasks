#!/bin/bash
set -e
cd /home/user

pip install --upgrade -r /home/user/devops/requirements.txt && pip freeze > /home/user/devops/pip-freeze.log
cat /home/user/devops/pip-freeze.log
