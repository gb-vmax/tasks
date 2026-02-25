#!/bin/bash
set -e
cd /home/user

grep -n '<script' /home/user/projects/i18n/en_US.po -A 2 -B 3
sed -i 's/msgstr "Welcome to our site! <script>alert('\''XSS'\'');<\/script>"/msgstr "Welcome to our site! "/' /home/user/projects/i18n/en_US.po
echo -e "DATE: $(date '+%Y-%m-%d %H:%M:%S')\nMSGID: greeting\nORIGINAL: Welcome to our site! <script>alert('XSS');</script>\nSANITIZED: Welcome to our site! " > /home/user/projects/i18n/update_log.txt
cat /home/user/projects/i18n/en_US.po /home/user/projects/i18n/update_log.txt
