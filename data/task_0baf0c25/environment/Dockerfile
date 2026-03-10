FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

cat > /home/user/disk_report.txt << 'EOF'
Filesystem         Size   Used   Avail  Use%  Mounted_on
/dev/sda1          500G   120G   380G   24%   /
/dev/sda2          200G   170G   30G    85%   /boot
/dev/sdb1          1.0T   900G   124G   90%   /data
/dev/sdc1          750G   200G   550G   27%   /backup
/dev/sdc2          300G   294G   6G     98%   /var/log
/dev/sdd1          400G   312G   88G    78%   /tmp
/dev/sdd2          600G   480G   120G   80%   /home
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
