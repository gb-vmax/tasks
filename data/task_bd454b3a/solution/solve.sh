#!/bin/bash
set -e
cd /home/user

find /home/user/webapp -type f | sort
find /home/user/webapp -type f \( -name "*.cache" -o -name "*.bak" \) | xargs rm -f
find /home/user/webapp -type f -name "*.log" | xargs gzip
find /home/user/webapp -type f -name "*.html" | xargs -I{} bash -c 'echo "<!-- deployed: v2.4.1 -->" >> "{}"'
files=$(find /home/user/webapp -type f \( -name "*.js" -o -name "*.css" \) | sed 's|/home/user/webapp/||' | sort)
count=$(echo "$files" | wc -l)
{ echo "=== Deploy Manifest ==="; echo "$files"; echo "=== Total: $count files ==="; } > /home/user/webapp/deploy_manifest.txt
cat /home/user/webapp/deploy_manifest.txt
echo "=== Cache/Bak files ===" && find /home/user/webapp -type f \( -name "*.cache" -o -name "*.bak" \) && echo "=== Log files ===" && find /home/user/webapp -type f -name "*.log" && echo "=== Log.gz files ===" && find /home/user/webapp -type f -name "*.log.gz" && echo "=== HTML last lines ===" && find /home/user/webapp -type f -name "*.html" -exec sh -c 'echo "$1:"; tail -1 "$1"' _ {} \;
