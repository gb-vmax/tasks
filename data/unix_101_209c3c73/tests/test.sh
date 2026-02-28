#!/bin/bash
if [ -f /home/user/docs/report.txt ] && [ ! -f /home/user/docs/report.txt.bz2 ] && grep -q 'Q1 Results: 100' /home/user/docs/report.txt; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
