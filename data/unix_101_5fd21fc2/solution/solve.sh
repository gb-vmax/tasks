#!/bin/bash
renice 5 -p $(cat /home/user/sleeppid.txt)
