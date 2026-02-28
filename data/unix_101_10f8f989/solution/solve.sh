#!/bin/bash
ps -u $(whoami) -o pid= > /home/user/my_pids.txt
