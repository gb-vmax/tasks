#!/bin/bash
set -e
cd /home/user

(grep 'ERROR' /home/user/microservice_logs/api.log | sed 's/^/API.LOG: /'; grep 'ERROR' /home/user/microservice_logs/db.log | sed 's/^/DB.LOG: /'; grep 'ERROR' /home/user/microservice_logs/cache.log | sed 's/^/CACHE.LOG: /') > /home/user/microservice_logs/error_summary.log
cat /home/user/microservice_logs/error_summary.log
