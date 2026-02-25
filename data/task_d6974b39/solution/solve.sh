#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/qa_project_env
python3 -m venv /home/user/qa_project_env/venv
/home/user/qa_project_env/venv/bin/python --version > /home/user/qa_project_env/python_version.txt
cat /home/user/qa_project_env/python_version.txt
