#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/dev_project/{src,tests,docs,data} && mv /home/user/dev_project/main.py /home/user/dev_project/src/main.py && mv /home/user/dev_project/utils.py /home/user/dev_project/src/utils.py && mv /home/user/dev_project/test_main.py /home/user/dev_project/tests/test_main.py && mv /home/user/dev_project/README.md /home/user/dev_project/docs/README.md && mv /home/user/dev_project/data.csv /home/user/dev_project/data/data.csv && printf "Moved /home/user/dev_project/main.py to /home/user/dev_project/src/main.py\nMoved /home/user/dev_project/utils.py to /home/user/dev_project/src/utils.py\nMoved /home/user/dev_project/test_main.py to /home/user/dev_project/tests/test_main.py\nMoved /home/user/dev_project/README.md to /home/user/dev_project/docs/README.md\nMoved /home/user/dev_project/data.csv to /home/user/dev_project/data/data.csv\n" > /home/user/dev_project/organization_log.txt
cat /home/user/dev_project/organization_log.txt
