#!/bin/bash
csplit -f logpart_ -n 3 --suppress-matched /home/user/logs.txt '/ERROR/' '{*}'
