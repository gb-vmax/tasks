#!/bin/bash
flock /home/user/lockfile.lock -c "echo locked > /home/user/result.txt"
