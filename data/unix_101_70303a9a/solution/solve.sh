#!/bin/bash
lsof -p $(cat /home/user/run_pid.txt) > /home/user/pid_lsof.txt
