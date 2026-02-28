#!/bin/bash
zdiff /home/user/file1.txt.gz /home/user/file2.txt > /home/user/zdiff_output.txt
# Should show the line difference (carrot vs carrots)
grep -q 'carrot' /home/user/zdiff_output.txt && grep -q 'carrots' /home/user/zdiff_output.txt && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
