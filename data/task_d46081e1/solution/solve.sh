#!/bin/bash
set -e
cd /home/user

cut -d, -f1,3 /home/user/app_translations.csv > /home/user/app_translations_es.csv && cat /home/user/app_translations_es.csv
