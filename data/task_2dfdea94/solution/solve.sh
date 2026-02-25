#!/bin/bash
set -e
cd /home/user

for f in /home/user/builds/output/*; do bn=$(basename "$f"); if [ -e "/home/user/artifacts/$bn" ]; then echo "$bn" >> /home/user/artifacts/move_errors.log; else mv "$f" /home/user/artifacts/; fi; done
cat /home/user/artifacts/move_errors.log
