#!/bin/bash
printf -v RESULT '%q' 'hello world!' && echo "$RESULT" > /home/user/quoted.txt
