#!/bin/bash
set -e
cd /home/user

find /home/user/build_output -type f -name "*.o" | while IFS= read -r orig_path; do rel_path="${orig_path#/home/user/build_output/}"; dest_path="/home/user/build_output/obj_archive/$rel_path"; mkdir -p "$(dirname "$dest_path")"; mv "$orig_path" "$dest_path"; echo "$orig_path -> $dest_path"; done > /home/user/build_output/obj_archive/move-log.txt
mkdir -p /home/user/build_output/obj_archive
find /home/user/build_output -type f -name "*.o" | while IFS= read -r orig_path; do rel_path="${orig_path#/home/user/build_output/}"; dest_path="/home/user/build_output/obj_archive/$rel_path"; mkdir -p "$(dirname "$dest_path")"; mv "$orig_path" "$dest_path"; echo "$orig_path -> $dest_path"; done > /home/user/build_output/obj_archive/move-log.txt
cat /home/user/build_output/obj_archive/move-log.txt
find /home/user/build_output -type f -name "*.o"
