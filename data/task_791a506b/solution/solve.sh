#!/bin/bash
set -e
cd /home/user

export MICROSERVICE_ENV=staging && echo $MICROSERVICE_ENV && echo "MICROSERVICE_ENV=staging" > /home/user/config_logs/env_setting.log
cat /home/user/config_logs/env_setting.log
