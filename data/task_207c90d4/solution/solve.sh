#!/bin/bash
set -e
cd /home/user

python2 /home/user/legacy_app/collect_info.py > /home/user/legacy_app/diagnostics.log
head -n 4 /home/user/legacy_app/diagnostics.log
