#!/bin/bash
set -e
cd /home/user

awk '!/^[[:space:]]*#/ && /^[[:space:]]*net_[^=]*=/' /home/user/system/config/settings.conf | awk -F'#' '{print $1}' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' > /home/user/system/logs/net_settings.log
mkdir -p /home/user/system/logs
awk '!/^[[:space:]]*#/ && /^[[:space:]]*net_[^=]*=/' /home/user/system/config/settings.conf | awk -F'#' '{print $1}' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' > /home/user/system/logs/net_settings.log
cat /home/user/system/logs/net_settings.log
