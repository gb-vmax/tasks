#!/bin/bash
set -e
cd /home/user

ls /home/user/project/
cd /home/user/project && mkdir -p src scripts docs config logs data && mv main.c utils.c parser.c utils.h parser.h config.h src/ && mv build.py deploy.py test_runner.py scripts/ && mv README.md CHANGELOG.md API.md docs/ && mv app.conf db.conf logging.conf config/ && mv app.log error.log debug.log logs/ && mv seed.sql schema.sql fixtures.json data/
chmod 644 /home/user/project/src/* && chmod 755 /home/user/project/scripts/* && chmod 644 /home/user/project/docs/* && chmod 600 /home/user/project/config/* && chmod 640 /home/user/project/logs/* && chmod 644 /home/user/project/data/*
cd /home/user/project && ln -s config/app.conf project.conf && ln -s scripts/build.py run.py && ln -s logs/app.log latest.log
cd /home/user/project && find . -type f ! -name 'manifest.txt' | sed 's|^\./||' | sort | while read f; do perm=$(stat -c '%a' "$f"); echo "$f $perm"; done > manifest.txt
cat /home/user/project/manifest.txt
ls -la /home/user/project/ && echo "---" && ls -la /home/user/project/src/ /home/user/project/scripts/ /home/user/project/config/ /home/user/project/logs/
