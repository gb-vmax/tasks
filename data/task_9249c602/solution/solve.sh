#!/bin/bash
set -e
cd /home/user

tail -n +2 /home/user/data/users.csv | cut -d, -f2 | sed 's/^[ \t]*//;s/[ \t]*$//' | grep -v '^$' > /home/user/data/emails.txt
cat /home/user/data/emails.txt
