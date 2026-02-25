#!/bin/bash
set -euo pipefail

# Create virtual environment
python3 -m venv /home/user/diskmon-env

# Activate it and install packages
source /home/user/diskmon-env/bin/activate
pip install psutil==5.9.8 click==8.1.7

# Save pip freeze output to log
pip freeze > /home/user/diskmon-env/pip-freeze.log

deactivate
