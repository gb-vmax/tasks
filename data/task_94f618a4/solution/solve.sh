#!/bin/bash
set -e
cd /home/user

mkdir -p pyutils
cd pyutils

python3 -m venv venv

./venv/bin/pip install --upgrade pip
./venv/bin/pip install requests==2.31.0 pytz==2024.1

printf '%s\n' 'pytz==2024.1' 'requests==2.31.0' > package_list.txt
