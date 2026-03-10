FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the project directory
mkdir -p /home/user/project

# Create all 20 expected files as empty files
touch /home/user/project/main.c
touch /home/user/project/utils.c
touch /home/user/project/parser.c
touch /home/user/project/utils.h
touch /home/user/project/parser.h
touch /home/user/project/config.h
touch /home/user/project/build.py
touch /home/user/project/deploy.py
touch /home/user/project/test_runner.py
touch /home/user/project/README.md
touch /home/user/project/CHANGELOG.md
touch /home/user/project/API.md
touch /home/user/project/app.conf
touch /home/user/project/db.conf
touch /home/user/project/logging.conf
touch /home/user/project/app.log
touch /home/user/project/error.log
touch /home/user/project/debug.log
touch /home/user/project/seed.sql
touch /home/user/project/schema.sql
touch /home/user/project/fixtures.json

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
