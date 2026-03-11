FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create project directory structure
mkdir -p /home/user/project/logs_archive
mkdir -p /home/user/project/src/auth
mkdir -p /home/user/project/src/api
mkdir -p /home/user/project/build

# Create .py files
echo "# main" > /home/user/project/src/main.py
echo "# utils" > /home/user/project/src/utils.py
echo "# login" > /home/user/project/src/auth/login.py
echo "# routes" > /home/user/project/src/api/routes.py

# Create .log files
echo "debug log" > /home/user/project/src/debug.log
echo "auth log" > /home/user/project/src/auth/auth.log
echo "build output" > /home/user/project/build/output.log
echo "build errors" > /home/user/project/build/errors.log

# Create .tmp files
echo "temp session" > /home/user/project/src/session.tmp
echo "temp cache" > /home/user/project/src/auth/cache.tmp
echo "temp request" > /home/user/project/src/api/request.tmp
echo "temp build" > /home/user/project/build/build.tmp

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
