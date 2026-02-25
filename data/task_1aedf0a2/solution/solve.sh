#!/bin/bash
set -e
cd /home/user

grep -w 'ERROR' /home/user/microservices/logs/service-api.log > /home/user/microservices/logs/error_summary.txt && grep -w 'ERROR' /home/user/microservices/logs/service-api.log | wc -l | xargs -I {} echo "Total ERROR lines: {}" >> /home/user/microservices/logs/error_summary.txt
cat /home/user/microservices/logs/error_summary.txt
