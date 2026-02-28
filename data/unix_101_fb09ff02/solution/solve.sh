#!/bin/bash
awk -F, '{print $1}' /home/user/data.csv > /home/user/first_column.txt
