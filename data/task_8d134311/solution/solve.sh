#!/bin/bash
set -e
cd /home/user

awk -v OFS= -v log="/home/user/project/artifact_verification.log" '
    /^\[/  { section=substr($0,2,length($0)-2); next }
    /^[[:space:]]*version[[:space:]]*=[[:space:]]*/ { version=$3; next }
    /^[[:space:]]*path[[:space:]]*=[[:space:]]*/ {
        path=$3;
        exists = (system("[ -f \"" path "\" ]") == 0 ? "yes" : "no");
        print "artifact:", section, " version:", version, " path:", path, " exists:", exists
    }
' /home/user/project/artifacts.ini > /home/user/project/artifact_verification.log
awk '
    /^\[.*\]$/    { section=substr($0,2,length($0)-2); next }
    /^[[:space:]]*version[[:space:]]*=/ {
        sub(/^[[:space:]]*version[[:space:]]*=[[:space:]]*/, "", $0);
        version=$0;
        gsub(/^[[:space:]]+|[[:space:]]+$/, "", version)
        next
    }
    /^[[:space:]]*path[[:space:]]*=/ {
        sub(/^[[:space:]]*path[[:space:]]*=[[:space:]]*/, "", $0);
        path=$0;
        gsub(/^[[:space:]]+|[[:space:]]+$/, "", path)
        exists = (system("[ -f \"" path "\" ]") == 0 ? "yes" : "no");
        print "artifact:" section " version:" version " path:" path " exists:" exists
    }
' /home/user/project/artifacts.ini > /home/user/project/artifact_verification.log
cat /home/user/project/artifact_verification.log
