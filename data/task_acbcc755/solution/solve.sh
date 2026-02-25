#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/docs_project/archive/
gzip -c /home/user/docs_project/final_drafts/chapter1.md > /home/user/docs_project/archive/chapter1.md.gz & gzip -c /home/user/docs_project/final_drafts/chapter2.md > /home/user/docs_project/archive/chapter2.md.gz & gzip -c /home/user/docs_project/final_drafts/chapter3.md > /home/user/docs_project/archive/chapter3.md.gz & wait
tar -cf /home/user/docs_project/archive/project_chapters_backup.tar -C /home/user/docs_project/archive chapter1.md.gz chapter2.md.gz chapter3.md.gz
mkdir -p /home/user/docs_project/restored/ && tar -xf /home/user/docs_project/archive/project_chapters_backup.tar -C /home/user/docs_project/restored/
find /home/user/docs_project/restored/ -maxdepth 1 -type f -name '*.gz' -printf '%f\n' | sort > /home/user/docs_project/extraction_log.txt
cat /home/user/docs_project/extraction_log.txt
