#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/project_env && touch /home/user/project_env/app.py /home/user/project_env/README.md && TZ="America/New_York" date '+%Y-%m-%d %H:%M:%S' > /tmp/project_env_datetime.txt && export LANG=de_DE.UTF-8 && export LC_ALL=de_DE.UTF-8 && locale | grep '^LANG=' > /tmp/project_env_lang.txt && printf "TIMEZONE: America/New_York\nDATETIME: %s\nLOCALE: %s\nFILES:\n- app.py %s\n- README.md %s\n" "$(cat /tmp/project_env_datetime.txt)" "$(cat /tmp/project_env_lang.txt)" "$(test -e /home/user/project_env/app.py && echo FOUND)" "$(test -e /home/user/project_env/README.md && echo FOUND)" > /home/user/project_env/env_report.txt
cat /home/user/project_env/env_report.txt
