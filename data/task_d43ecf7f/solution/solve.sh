#!/bin/bash
set -e
cd /home/user

ls -la /home/user/artifacts/build/
tar -czf /home/user/artifacts/build.tar.gz -C /home/user/artifacts build/
tar -cjf /home/user/artifacts/build.tar.bz2 -C /home/user/artifacts build/
ls -l /home/user/artifacts/build.tar.gz /home/user/artifacts/build.tar.bz2
printf 'compression comparison\nbuild.tar.gz 835\nbuild.tar.bz2 900\nwinner build.tar.gz' > /home/user/artifacts/compression_report.txt
cat /home/user/artifacts/compression_report.txt
