#!/bin/bash
set -e
cd /home/user

sort /home/user/data/training_text.txt | uniq -c | awk '{print $1 " " $2}' | sort -k2,2 > /home/user/data/word_frequency_report.txt
cat /home/user/data/word_frequency_report.txt
