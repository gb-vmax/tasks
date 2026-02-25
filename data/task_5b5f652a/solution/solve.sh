#!/bin/bash
set -e
cd /home/user

cp /home/user/localization_project/.env.example /home/user/localization_project/.env
sed -i 's/^LANG=.*/LANG=fr_FR/;s/^LANGUAGE=.*/LANGUAGE=fr/;s/^LC_ALL=.*/LC_ALL=fr_FR.UTF-8/' /home/user/localization_project/.env
export $(grep -E '^(LANG|LANGUAGE|LC_ALL)=' /home/user/localization_project/.env | xargs)
printf "Current LANG: %s\nCurrent LANGUAGE: %s\nCurrent LC_ALL: %s\n" "$LANG" "$LANGUAGE" "$LC_ALL" > /home/user/localization_project/locale_status.log
cat /home/user/localization_project/locale_status.log
