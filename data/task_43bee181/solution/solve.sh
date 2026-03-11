#!/bin/bash
set -e
cd /home/user

find /home/user/translations -type f | sort
mkdir -p /home/user/releases && tar -czf /home/user/releases/translations_v2.tar.gz -C /home/user translations/
tar -tzf /home/user/releases/translations_v2.tar.gz | grep -v '/$' | sort > /home/user/releases/translations_v2.manifest
echo "MD5: $(md5sum /home/user/releases/translations_v2.tar.gz | awk '{print $1}')" >> /home/user/releases/translations_v2.manifest
cat /home/user/releases/translations_v2.manifest
ls -lh /home/user/releases/ && tar -tzf /home/user/releases/translations_v2.tar.gz
