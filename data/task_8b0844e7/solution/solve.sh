#!/bin/bash
set -e
cd /home/user

ls -la /home/user/configs/active/ && ls -la /home/user/configs/versions/
ln -sf /home/user/configs/versions/nginx.conf.v2 /home/user/configs/active/nginx.conf
printf 'nginx.conf -> /home/user/configs/versions/nginx.conf.v2\n' > /home/user/configs/provision.log
ls -la /home/user/configs/active/ && cat /home/user/configs/provision.log
