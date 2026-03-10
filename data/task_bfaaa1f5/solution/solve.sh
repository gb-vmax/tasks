#!/bin/bash
set -e
cd /home/user

cat /home/user/app/config.env
cat /home/user/app/rotation_log.txt
OLD_KEY=$(grep '^API_KEY=' /home/user/app/config.env | cut -d'=' -f2)
OLD_KEY_SHORT="${OLD_KEY:0:8}"
TODAY=$(date +%Y-%m-%d)
NEW_KEY=$(echo -n "rotate-${TODAY}-secret" | openssl dgst -sha256 -hmac "prod-salt" | awk '{print $2}')
NEW_KEY_SHORT="${NEW_KEY:0:8}"
sed -i "s|^API_KEY=.*|API_KEY=${NEW_KEY}|" /home/user/app/config.env
echo "ROTATED API_KEY on ${TODAY} old=${OLD_KEY_SHORT} new=${NEW_KEY_SHORT}" >> /home/user/app/rotation_log.txt
echo "Done. Old key (first 8): ${OLD_KEY_SHORT}, New key (first 8): ${NEW_KEY_SHORT}"
cat /home/user/app/config.env && echo "---" && cat /home/user/app/rotation_log.txt
