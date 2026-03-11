#!/bin/bash
set -e
cd /home/user

cat /home/user/api_response.json
jq -r '.users | map(select(.status == "active")) | sort_by(.id) | ["id","username","email","first_name","last_name","department","created_at"], (.[] | [.id, .username, .email, .profile.first_name, .profile.last_name, .profile.department, .created_at]) | @csv' /home/user/api_response.json | sed 's/"//g' > /home/user/active_users.csv
python3 -c "
import json, csv

with open('/home/user/api_response.json') as f:
    data = json.load(f)

active = [u for u in data['users'] if u['status'] == 'active']
active.sort(key=lambda u: u['id'])

with open('/home/user/active_users.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id','username','email','first_name','last_name','department','created_at'])
    for u in active:
        writer.writerow([u['id'], u['username'], u['email'], u['profile']['first_name'], u['profile']['last_name'], u['profile']['department'], u['created_at']])

with open('/home/user/active_count.txt', 'w') as f:
    f.write(str(len(active)) + '\n')
"
cat /home/user/active_users.csv && echo "---" && cat /home/user/active_count.txt
