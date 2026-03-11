#!/bin/bash
set -e
cd /home/user

ls /home/user/network/configs/ && ls /home/user/network/active/
ln -s /home/user/network/configs/core-router.conf /home/user/network/active/core-router.conf
ln -s /home/user/network/configs/edge-router.conf /home/user/network/active/edge-router.conf
ln -s /home/user/network/configs/core-router.conf /home/user/network/active/primary.conf
printf 'core-router.conf -> /home/user/network/configs/core-router.conf\nedge-router.conf -> /home/user/network/configs/edge-router.conf\nprimary.conf -> /home/user/network/configs/core-router.conf\n' > /home/user/network/active/links.txt
readlink /home/user/network/active/core-router.conf && readlink /home/user/network/active/edge-router.conf && readlink /home/user/network/active/primary.conf && echo "---" && cat /home/user/network/active/links.txt
