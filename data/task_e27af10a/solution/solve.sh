#!/bin/bash
set -e
cd /home/user

grep -v '=unchanged$' /home/user/config/settings.cfg | cut -d= -f1 > /home/user/config/modified_keys.txt
cat /home/user/config/modified_keys.txt
