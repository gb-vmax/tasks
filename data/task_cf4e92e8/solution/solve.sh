#!/bin/bash
set -e
cd /home/user

grep -vxFf /home/user/original.conf /home/user/updated.conf | sed 's/^/ADDED: /' > /home/user/change.log
cat /home/user/change.log
