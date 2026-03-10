FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Add alice, bob, and charlie to /etc/passwd
echo "alice:x:1001:1001::/home/alice:/bin/bash" >> /etc/passwd
echo "bob:x:1002:1002::/home/bob:/bin/sh" >> /etc/passwd
echo "charlie:x:1500:1500::/home/charlie:/usr/sbin/nologin" >> /etc/passwd

# Ensure /home/user exists but /home/user/audit does NOT exist
mkdir -p /home/user
# Do NOT create /home/user/audit — the agent must create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
