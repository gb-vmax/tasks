#!/bin/bash
set -e
cd /home/user

grep ' 404 ' /home/user/logs/webserver_access.log > /home/user/logs/404_errors.log
cat /home/user/logs/404_errors.log
