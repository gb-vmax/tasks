#!/bin/bash
set -e
cd /home/user

awk -F, 'NR==1{for(i=1;i<=NF;i++) h[$i]=i} NR>1&&$h["status"]=="completed"{u[$h["user_id"] OFS $h["username"]]++} END{for(k in u) if(u[k]>3) print k, u[k]}' OFS="," /home/user/user_transactions.csv | sort -t, -k1,1n > /home/user/opt_users_counts.csv
cut -d, -f1 /home/user/opt_users_counts.csv > /home/user/opt_user_ids.txt
jq --argfile ids /home/user/opt_user_ids.txt '[.[] | select((.user_id|tostring) as $id | $id | IN($ids[])) | {user_id, email, sign_up_date, last_login}]' /home/user/user_profiles.json > /home/user/optimized_query_users.json
python3 -c "import json
ids = set(open('/home/user/opt_user_ids.txt').read().split())
with open('/home/user/user_profiles.json') as f: data = json.load(f)
out = [ {k:x[k] for k in ('user_id','email','sign_up_date','last_login')} for x in data if str(x['user_id']) in ids ]
with open('/home/user/optimized_query_users.json','w') as f: json.dump(out, f, indent=2)"
echo "user_id,username,completed_transaction_count" > /home/user/optimization_report.csv && awk -F, '{print $1","$2","$3}' /home/user/opt_users_counts.csv >> /home/user/optimization_report.csv
head /home/user/optimized_query_users.json /home/user/optimization_report.csv
