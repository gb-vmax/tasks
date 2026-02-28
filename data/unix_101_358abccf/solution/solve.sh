#!/bin/bash
cat /home/user/files.csv | xargs -d, wc -l > /home/user/linecounts.txt
