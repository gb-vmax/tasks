#!/bin/bash
dd if=/home/user/large.txt of=/home/user/partial.bin bs=6 count=2 status=none
