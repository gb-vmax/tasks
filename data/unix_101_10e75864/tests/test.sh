#!/bin/bash
if [ ! -f /home/user/file1.txt ] && [ ! -f /home/user/file2.txt ] && [ ! -f /home/user/file3.txt ] && [ -f /home/user/file4.txt ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
