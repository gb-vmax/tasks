#!/bin/bash
flock -n -E 42 /home/user/conflict.lock -c "echo test > /home/user/test.txt"
