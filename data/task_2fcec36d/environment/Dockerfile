FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

install -d -m 755 /home/user/dev_project

# Create the required files with arbitrary contents
echo "Project README" > /home/user/dev_project/README.md
echo "print('Hello from main.py')" > /home/user/dev_project/main.py
echo "def util_func(): pass" > /home/user/dev_project/utils.py
echo "def test_main(): pass" > /home/user/dev_project/test_main.py
echo "pytest" > /home/user/dev_project/requirements.txt
echo "col1,col2\n1,2" > /home/user/dev_project/data.csv

# Ensure no subdirectories are created yet
# Ensure no organization_log.txt is created

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
