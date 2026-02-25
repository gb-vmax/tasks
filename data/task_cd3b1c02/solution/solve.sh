#!/bin/bash
set -e
cd /home/user

mkdir -p ~/my_python_project/src ~/my_python_project/tests
printf ".\n./src\n./tests\n./project_structure.txt\n" > ~/my_python_project/project_structure.txt
cat ~/my_python_project/project_structure.txt
