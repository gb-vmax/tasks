#!/bin/bash
flock /home/user/lockfile.lock -c "echo 'locked append' >> /home/user/output.txt"
