#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/etl_project
python3 -m venv /home/user/etl_project/venv
sudo apt-get update && sudo apt-get install -y python3-venv
python3 -m venv /home/user/etl_project/venv
/home/user/etl_project/venv/bin/pip install pandas==1.4.2 requests==2.27.1 pyarrow==8.0.0
/home/user/etl_project/venv/bin/pip freeze > /home/user/etl_project/requirements-locked.txt
cat > /home/user/etl_project/etl_test.py << EOF
import pandas
import requests
import pyarrow

print(f"pandas: {pandas.__version__}")
print(f"requests: {requests.__version__}")
print(f"pyarrow: {pyarrow.__version__}")
EOF
/home/user/etl_project/venv/bin/python /home/user/etl_project/etl_test.py > /home/user/etl_project/etl_test_output.log
/home/user/etl_project/venv/bin/pip install numpy==1.21.6
/home/user/etl_project/venv/bin/pip freeze > /home/user/etl_project/requirements-locked.txt
/home/user/etl_project/venv/bin/python /home/user/etl_project/etl_test.py > /home/user/etl_project/etl_test_output.log
