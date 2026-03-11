FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

cat > /home/user/config_changes.log << 'EOF'
[2024-06-10 08:14:02] USER=alice COMPONENT=database ACTION=update STATUS=success
[2024-06-10 08:45:17] USER=bob COMPONENT=webserver ACTION=update STATUS=success
[2024-06-10 09:02:33] USER=alice COMPONENT=network ACTION=update STATUS=failure
[2024-06-10 09:30:55] USER=bob COMPONENT=network ACTION=rollback STATUS=failure
[2024-06-10 10:11:08] USER=carol COMPONENT=database ACTION=update STATUS=success
[2024-06-10 10:45:22] USER=alice COMPONENT=firewall ACTION=update STATUS=success
[2024-06-10 11:03:41] USER=carol COMPONENT=webserver ACTION=update STATUS=success
[2024-06-10 11:28:59] USER=bob COMPONENT=database ACTION=rollback STATUS=success
[2024-06-10 12:00:05] USER=alice COMPONENT=webserver ACTION=update STATUS=success
[2024-06-10 13:15:44] USER=carol COMPONENT=firewall ACTION=update STATUS=failure
[2024-06-10 14:02:30] USER=alice COMPONENT=database ACTION=update STATUS=success
[2024-06-10 14:55:13] USER=bob COMPONENT=firewall ACTION=update STATUS=success
[2024-06-10 15:30:27] USER=carol COMPONENT=network ACTION=update STATUS=success
[2024-06-10 16:10:09] USER=alice COMPONENT=network ACTION=rollback STATUS=failure
[2024-06-10 16:48:52] USER=bob COMPONENT=webserver ACTION=update STATUS=failure
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
