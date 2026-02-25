#!/bin/bash
set -e
cd /home/user

tar -xzf /home/user/locales_update.tar.gz -C /home/user
find /home/user/locales -maxdepth 1 -type f -exec basename {} \; | sort > /home/user/locales_extraction.log
