#!/bin/bash
jq -S -s 'add' /home/user/data1.json /home/user/data2.json > /home/user/merged.json
