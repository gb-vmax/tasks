#!/bin/bash
dd if=/home/user/data.txt of=/home/user/second_line.txt bs=6 skip=1 count=1 status=none
