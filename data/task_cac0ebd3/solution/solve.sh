#!/bin/bash
set -e
cd /home/user

find /home/user/artifacts/ -type f \( -name "*.bin" -o -name "*.so" \)
mkdir -p /home/user/backup
find /home/user/artifacts/ -type f \( -name "*.bin" -o -name "*.so" \) | sed 's|/home/user/artifacts/||' | tar -czf /home/user/backup/release_bundle.tar.gz -C /home/user/artifacts/ -T -
tar -tzf /home/user/backup/release_bundle.tar.gz
cd /home/user/backup && sha256sum release_bundle.tar.gz > release_bundle.tar.gz.sha256
cat /home/user/backup/release_bundle.tar.gz.sha256
find /home/user/artifacts/ -type f \( -name "*.bin" -o -name "*.so" \) -printf "%P %s\n" | sort > /home/user/backup/MANIFEST.txt
cat /home/user/backup/MANIFEST.txt
cd /home/user/backup && sha256sum -c release_bundle.tar.gz.sha256
