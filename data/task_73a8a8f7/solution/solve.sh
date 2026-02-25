#!/bin/bash
set -e
cd /home/user

printf "MAX_CPU=8\nMAX_MEM_GB=32\nSTORAGE_TB=10\n" > /home/user/.env.capacity
set -a && . /home/user/.env.capacity && set +a && printf "Resources: CPU=%s MEM=%sGB STORAGE=%sTB\n" "$MAX_CPU" "$MAX_MEM_GB" "$STORAGE_TB" > /home/user/capacity_output.log
cat /home/user/capacity_output.log
