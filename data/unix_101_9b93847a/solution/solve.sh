#!/bin/bash
flock /home/user/lockfile.lock -c 'echo locked >> /home/user/lockfile.log'
