FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the applogs directory structure
mkdir -p /home/user/applogs/web /home/user/applogs/db /home/user/applogs/cron

# Create log files with exact content and sizes
python3 -c "open('/home/user/applogs/web/access.log','wb').write(b'a'*15000)"
python3 -c "open('/home/user/applogs/web/debug.log','wb').write(b'b'*8000)"
python3 -c "open('/home/user/applogs/web/error.log','wb').write(b'c'*12500)"
python3 -c "open('/home/user/applogs/db/queries.log','wb').write(b'd'*20000)"
python3 -c "open('/home/user/applogs/db/slow.log','wb').write(b'e'*10240)"
python3 -c "open('/home/user/applogs/cron/tasks.log','wb').write(b'f'*11000)"
python3 -c "open('/home/user/applogs/cron/archive.log','wb').write(b'g'*500)"

# Do NOT create /home/user/backup — the test asserts it does not exist yet

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
