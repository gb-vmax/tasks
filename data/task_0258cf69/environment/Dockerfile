FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

cat > /home/user/user_transactions.csv <<EOF
user_id,username,transaction_id,amount,timestamp,status
1,alice,tx1001,49.95,2024-05-01T09:00:00Z,completed
1,alice,tx1002,9.99,2024-05-02T11:15:00Z,pending
1,alice,tx1003,29.00,2024-05-04T21:00:00Z,completed
1,alice,tx1004,17.50,2024-05-10T18:00:00Z,completed
2,bob,tx2011,99.99,2024-05-01T10:20:00Z,completed
2,bob,tx2012,14.50,2024-05-03T07:45:00Z,completed
2,bob,tx2013,17.00,2024-05-07T19:30:00Z,completed
2,bob,tx2014,23.75,2024-05-12T14:15:00Z,completed
2,bob,tx2015,30.25,2024-05-13T16:40:00Z,pending
3,charlie,tx3010,8.99,2024-05-07T13:57:00Z,completed
4,danielle,tx4201,44.00,2024-05-08T22:00:00Z,pending
5,emma,tx5101,25.00,2024-05-11T20:00:00Z,completed
5,emma,tx5102,29.99,2024-05-12T14:00:00Z,completed
5,emma,tx5103,17.75,2024-05-14T08:00:00Z,completed
5,emma,tx5104,15.25,2024-05-15T12:30:00Z,completed
EOF

cat > /home/user/user_profiles.json <<EOF
[
  {"user_id": 1, "email": "alice@example.com", "sign_up_date": "2022-11-01", "last_login": "2024-05-10"},
  {"user_id": 2, "email": "bob@example.com", "sign_up_date": "2022-10-15", "last_login": "2024-05-13"},
  {"user_id": 3, "email": "charlie@example.com", "sign_up_date": "2023-01-10", "last_login": "2024-05-08"},
  {"user_id": 4, "email": "danielle@example.com", "sign_up_date": "2023-03-09", "last_login": "2024-05-08"},
  {"user_id": 5, "email": "emma@example.com", "sign_up_date": "2022-12-25", "last_login": "2024-05-15"}
]
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
