#!/bin/bash
set -e
cd /home/user

ls -l /home/user/configs/database.conf
chmod 640 /home/user/configs/database.conf
echo 'PERMISSION_CHANGE: /home/user/configs/database.conf 664->640 by user' >> /home/user/configs/audit.log
ls -l /home/user/configs/database.conf && tail -1 /home/user/configs/audit.log
