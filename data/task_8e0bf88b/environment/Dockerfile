FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/fileserver/{tmp,uploads,scripts,reports,archive}

# Old .tmp files (3 days ago)
echo "old session" > /home/user/fileserver/tmp/session_old.tmp
echo "old cache"   > /home/user/fileserver/tmp/cache_old.tmp
echo "old scratch" > /home/user/fileserver/uploads/scratch_old.tmp
touch -d "3 days ago" /home/user/fileserver/tmp/session_old.tmp
touch -d "3 days ago" /home/user/fileserver/tmp/cache_old.tmp
touch -d "3 days ago" /home/user/fileserver/uploads/scratch_old.tmp

# Recent .tmp file (1 day ago)
echo "new session" > /home/user/fileserver/tmp/session_new.tmp
touch -d "1 day ago" /home/user/fileserver/tmp/session_new.tmp

# World-writable .sh files
printf '#!/bin/bash\necho deploy\n' > /home/user/fileserver/scripts/deploy.sh
printf '#!/bin/bash\necho backup\n' > /home/user/fileserver/scripts/backup.sh
chmod 0777 /home/user/fileserver/scripts/deploy.sh
chmod 0777 /home/user/fileserver/scripts/backup.sh

# Non-world-writable .sh file
printf '#!/bin/bash\necho monitor\n' > /home/user/fileserver/scripts/monitor.sh
chmod 0755 /home/user/fileserver/scripts/monitor.sh

# Old .report files (3 days ago)
echo "Q1 Sales"  > /home/user/fileserver/reports/q1_sales.report
echo "Q2 Sales"  > /home/user/fileserver/reports/q2_sales.report
echo "Health OK" > /home/user/fileserver/reports/system_health.report
touch -d "3 days ago" /home/user/fileserver/reports/q1_sales.report
touch -d "3 days ago" /home/user/fileserver/reports/q2_sales.report
touch -d "3 days ago" /home/user/fileserver/reports/system_health.report

# Recent .report file (1 day ago)
echo "Q3 Sales" > /home/user/fileserver/reports/q3_sales.report
touch -d "1 day ago" /home/user/fileserver/reports/q3_sales.report

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
