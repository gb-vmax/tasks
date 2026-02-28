#!/bin/bash
pass=1
# Check that file1.txt and subdir/file2.txt exist and have correct content
if ! [ -f /home/user/projectB/file1.txt ] || ! diff /home/user/projectA/file1.txt /home/user/projectB/file1.txt >/dev/null; then pass=0; fi
if ! [ -f /home/user/projectB/subdir/file2.txt ] || ! diff /home/user/projectA/subdir/file2.txt /home/user/projectB/subdir/file2.txt >/dev/null; then pass=0; fi
# Check that old.txt and subdir/extra.txt have been deleted
if [ -f /home/user/projectB/old.txt ] || [ -f /home/user/projectB/subdir/extra.txt ]; then pass=0; fi
echo $pass > /logs/verifier/reward.txt
