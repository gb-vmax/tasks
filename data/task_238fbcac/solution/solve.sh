#!/bin/bash
set -e
cd /home/user

grep 'ERROR' /home/user/logs/nginx_app.log | tee /home/user/logs/nginx_error_lines.txt
cat /home/user/logs/nginx_error_lines.txt
