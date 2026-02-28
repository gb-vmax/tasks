#!/bin/bash
if [ ! -f /home/user/story_modified.txt ]; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if grep -q 'cat' /home/user/story_modified.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if ! grep -q 'dog sat on the mat.' /home/user/story_modified.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
if ! grep -q 'A black dog chased a rat.' /home/user/story_modified.txt; then echo 0 > /logs/verifier/reward.txt; exit 0; fi
echo 1 > /logs/verifier/reward.txt
