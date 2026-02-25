#!/bin/bash
set -e
cd /home/user

awk -F, 'NR>1 { if ($3+0 > max[$1]) max[$1]=$3+0 } END { for (app in max) print app, max[app] }' /home/user/profile_data/app_memory.csv | jq -Rn '[inputs|split(" ")|{(.[0]): (.[1]|tonumber)}]|add' > /home/user/profile_data/max_memory_per_app.json
awk -F, '
NR > 1 {
    if ($3+0 > max[$1]) max[$1]=$3+0
    apps[$1]=1
}
END {
    printf "{"
    n = 0
    for (app in apps) n++
    i = 0
    for (app in apps) {
        printf "\"%s\": %d", app, max[app]
        i++
        if (i < n) printf ", "
    }
    print "}"
}
' /home/user/profile_data/app_memory.csv > /home/user/profile_data/max_memory_per_app.json
cat /home/user/profile_data/max_memory_per_app.json
