#!/bin/bash
set -e
cd /home/user

find /home/user/logs -type f -perm -o=w -print > /home/user/logs/world_writable_scan.txt
cat /home/user/logs/world_writable_scan.txt
