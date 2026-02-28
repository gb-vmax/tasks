#!/bin/bash
fgrep -f /home/user/patterns.txt /home/user/animals.txt | wc -l > /home/user/match_count.txt
