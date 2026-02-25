#!/bin/bash
set -e
cd /home/user

sqlite3 -header -csv /home/user/projects/tasks.db "SELECT id,filename,project,date_added FROM files;"
