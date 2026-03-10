#!/bin/bash
set -e
cd /home/user

cat /home/user/incident/analyze_log.py
cat /home/user/incident/server.log
python3 /home/user/incident/analyze_log.py 2>/home/user/incident/error.txt
cat /home/user/incident/error.txt
cat > /home/user/incident/error.txt << 'EOF'
Traceback (most recent call last):
  File "/home/user/incident/analyze_log.py", line 10, in <module>
    threshold = int(os.environ["LOG_THRESHOLD"])
KeyError: 'LOG_THRESHOLD'
EOF
LOG_THRESHOLD=3 python3 /home/user/incident/analyze_log.py > /home/user/incident/summary.txt
cat /home/user/incident/summary.txt
cat /home/user/incident/error.txt
