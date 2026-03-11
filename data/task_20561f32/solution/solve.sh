#!/bin/bash
set -e
cd /home/user

ls -la /home/user/utils/
cat /home/user/utils/word_freq.py
chmod +x /home/user/utils/word_freq.py && /home/user/utils/word_freq.py /home/user/utils/sample.txt > /home/user/utils/report.txt
cat /home/user/utils/report.txt
