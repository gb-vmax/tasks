#!/bin/bash
grep -i -c 'error' /home/user/logs/server.log > /home/user/error_count.txt
