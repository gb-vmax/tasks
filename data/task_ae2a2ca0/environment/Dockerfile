FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create webapp directory structure
mkdir -p /home/user/webapp/config /home/user/webapp/public /home/user/webapp/static /home/user/webapp/logs

# Create files with specified permissions
touch /home/user/webapp/index.php && chmod 644 /home/user/webapp/index.php
touch /home/user/webapp/config/settings.cfg && chmod 666 /home/user/webapp/config/settings.cfg
touch /home/user/webapp/config/database.cfg && chmod 640 /home/user/webapp/config/database.cfg
touch /home/user/webapp/public/upload.php && chmod 777 /home/user/webapp/public/upload.php
touch /home/user/webapp/public/index.html && chmod 644 /home/user/webapp/public/index.html
touch /home/user/webapp/static/style.css && chmod 622 /home/user/webapp/static/style.css
touch /home/user/webapp/static/logo.png && chmod 644 /home/user/webapp/static/logo.png
touch /home/user/webapp/logs/app.log && chmod 640 /home/user/webapp/logs/app.log

# Do NOT create /home/user/diagnostics — the agent will create it
# Do NOT create security_scan.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
