#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/datasets/train /home/user/datasets/test /home/user/datasets/validation && printf "/home/user/datasets/train\n/home/user/datasets/test\n/home/user/datasets/validation\n" > /home/user/dataset_summary.txt
cat /home/user/dataset_summary.txt
