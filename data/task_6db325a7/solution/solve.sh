#!/bin/bash
set -e
cd /home/user

grep -w -e 'chmod' -e 'chown' /home/user/logs/auth_sample.log > /home/user/logs/perm_audit.log
cat /home/user/logs/perm_audit.log
