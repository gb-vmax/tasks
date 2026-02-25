#!/bin/bash
set -e
cd /home/user

find /home/user/app_profile/results/ -maxdepth 1 -type f -name "*.prof" -printf '%f %s $(date -u -d @%T@ +%Y-%m-%dT%H:%M:%SZ)\n' | sed -E "s/\ ([0-9]+)\ \\\$\(date\ -u\ -d\ \@([0-9]+)\@\ \+%Y-%m-%dT%H:%M:%SZ\)/ \1 \$(date -u -d \@\2\ +%Y-%m-%dT%H:%M:%SZ)/" | while read f size m; do echo "$f $size $(date -u -r /home/user/app_profile/results/$f +%Y-%m-%dT%H:%M:%SZ)"; done | sort > /tmp/profile_src_list.txt
find /home/user/remote_server/backup/results/ -maxdepth 1 -type f -name "*.prof" -printf '%f %s\n' | while read f size; do if [ -e /home/user/remote_server/backup/results/$f ]; then echo "$f $size $(date -u -r /home/user/remote_server/backup/results/$f +%Y-%m-%dT%H:%M:%SZ)"; fi; done | sort > /tmp/profile_tgt_list.txt
awk '
BEGIN {
    while ((getline < "/tmp/profile_tgt_list.txt") > 0) {
        tgt[$1] = $0
    }
    close("/tmp/profile_tgt_list.txt")
}
{
    src[$1] = $0
    if (!($1 in tgt))
        print "COPIED "$1
    else {
        n=split(tgt[$1],tgtarr," "); split($0,srcarr," ");
        if (tgtarr[2]!=srcarr[2] || tgtarr[3]!=srcarr[3])
            print "UPDATED "$1
    }
}
END {
    for (f in tgt)
        if (!(f in src))
            print "DELETED "f
}
' /tmp/profile_src_list.txt | sort > /tmp/profile_sync_ops.txt
while read op file; do
  if [ "$op" = "COPIED" ] || [ "$op" = "UPDATED" ]; then
    cp -p "/home/user/app_profile/results/$file" "/home/user/remote_server/backup/results/$file"
  elif [ "$op" = "DELETED" ]; then
    rm -f "/home/user/remote_server/backup/results/$file"
  fi
done < /tmp/profile_sync_ops.txt
find /home/user/remote_server/backup/results/ -maxdepth 1 -type f -name "*.prof" -printf '%f %s\n' | while read f size; do if [ -e /home/user/remote_server/backup/results/$f ]; then echo "$f $size $(date -u -r /home/user/remote_server/backup/results/$f +%Y-%m-%dT%H:%M:%SZ)"; fi; done | sort > /tmp/profile_tgt_list_after.txt
(echo "[BEFORE]"; cat /tmp/profile_src_list.txt; echo; echo "[SYNC OPERATIONS]"; cat /tmp/profile_sync_ops.txt; echo; echo "[AFTER]"; cat /tmp/profile_tgt_list_after.txt) > /home/user/sync_report.log
cat /home/user/sync_report.log
