#!/bin/bash
set -e
cd /home/user

cat /home/user/backups/backup_run.log
awk -F'|' 'BEGIN{n=0;total=0;print "=== RESTORE VERIFICATION REPORT ===";print "Successful backups eligible for restore testing:";print ""} /^BACKUP/ && $4=="SUCCESS" && $5+0>1000{id[n]=$2;host[n]=$3;size[n]=$5+0;dur[n]=$6+0;total+=$5+0;n++} END{for(i=0;i<n;i++){printf "  %-8s%-20s%4d MB   (%3d sec)\n",id[i],host[i],size[i],dur[i]};print "";printf "Total eligible: %d jobs, %d MB\n",n,total}' /home/user/backups/backup_run.log > /home/user/backups/restore_verification.txt
cat /home/user/backups/restore_verification.txt
