#!/bin/bash
IFS=: read -a ARR < /home/user/env/colors.txt; echo "${ARR[2]}" > /home/user/env/third_color.txt
