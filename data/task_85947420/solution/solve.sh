#!/bin/bash
set -e
cd /home/user

awk '/^\[Database\]/{flag=1;next}/^\[.*\]/{flag=0}flag && /^[^;#].*=.*$/ { sub(/^[ \t]+/, "", $0); sub(/[ \t]+$/, "", $0); print }' /home/user/server_configs/prod_server.ini
