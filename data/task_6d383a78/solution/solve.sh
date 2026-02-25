#!/bin/bash
set -e
cd /home/user

find /home/user/docs -type f -name '*.md' -exec basename {} .md \; | sort -u > /home/user/doc_summary.txt
cat /home/user/doc_summary.txt
