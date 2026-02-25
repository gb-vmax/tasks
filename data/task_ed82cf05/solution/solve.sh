#!/bin/bash
set -e
cd /home/user

if [ ! -f /home/user/target-repo/.gitmodules ] || ! grep -q '\[submodule "' /home/user/target-repo/.gitmodules; then echo "No submodules found." > /home/user/target-repo/submodules_list.txt; else awk '/\[submodule /{getline; path=$0; getline; url=$0; sub(/^[ \t]*path = /,"",path); sub(/^[ \t]*url = /,"",url); print "path: " path ", url: " url}' /home/user/target-repo/.gitmodules > /home/user/target-repo/submodules_list.txt; fi
cat /home/user/target-repo/submodules_list.txt
