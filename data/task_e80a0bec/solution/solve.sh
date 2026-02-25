#!/bin/bash
set -e
cd /home/user

chmod 700 /home/user/microservices/orderservice/start.sh && chmod 700 /home/user/microservices/orderservice && (stat -c "%A %n" /home/user/microservices/orderservice/start.sh; stat -c "%A %n" /home/user/microservices/orderservice) > /home/user/microservices/orderservice/permissions_report.log
cat /home/user/microservices/orderservice/permissions_report.log
