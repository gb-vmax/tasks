#!/bin/bash
pass=1
if [ ! -d /home/user/backup_dir ]; then pass=0; fi
if [ ! -f /home/user/backup_dir/sub/b.txt ]; then pass=0; fi
if ! cmp -s /home/user/source_dir/a.txt /home/user/backup_dir/a.txt; then pass=0; fi
if ! cmp -s /home/user/source_dir/sub/b.txt /home/user/backup_dir/sub/b.txt; then pass=0; fi
if [ "$(stat -c '%a' /home/user/backup_dir/a.txt)" != "700" ]; then pass=0; fi
if [ "$(stat -c '%a' /home/user/backup_dir/sub/b.txt)" != "600" ]; then pass=0; fi
if [ "$(date -r /home/user/backup_dir/a.txt +%Y%m%d%H%M)" != "202101010101" ]; then pass=0; fi
if [ "$(date -r /home/user/backup_dir/sub/b.txt +%Y%m%d%H%M)" != "202102020202" ]; then pass=0; fi
echo $pass > /logs/verifier/reward.txt
