#!/bin/bash
export MYVAR=hello_export && env | grep '^MYVAR=' > /home/user/out.txt
