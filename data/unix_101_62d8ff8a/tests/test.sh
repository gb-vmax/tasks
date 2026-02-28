#!/bin/bash
pass=1
if [ ! -d /home/user/project_copy/src ]; then pass=0; fi
if [ ! -f /home/user/project_copy/src/main.c ]; then pass=0; fi
if [ ! -f /home/user/project_copy/README.md ]; then pass=0; fi
if [ "$(stat -c%a /home/user/project/src/main.c)" != "600" ]; then pass=0; fi
if [ "$(stat -c%a /home/user/project/README.md)" != "644" ]; then pass=0; fi
if [ "$(stat -c%Y /home/user/project/src/main.c)" != "$(stat -c%Y /home/user/project_copy/src/main.c)" ]; then pass=0; fi
if [ "$(stat -c%Y /home/user/project/README.md)" != "$(stat -c%Y /home/user/project_copy/README.md)" ]; then pass=0; fi
echo $pass > /logs/verifier/reward.txt
