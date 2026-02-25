#!/bin/bash
set -e
cd /home/user

python /home/user/integration_tests/legacy_api_test.py > /home/user/integration_tests/test_run.log 2>&1
python3 /home/user/integration_tests/legacy_api_test.py > /home/user/integration_tests/test_run.log 2>&1
cat /home/user/integration_tests/test_run.log
