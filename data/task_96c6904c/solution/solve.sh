#!/bin/bash
set -e
cd /home/user

cat /home/user/data/raw_samples.csv
awk -F',' 'BEGIN{print "id,feat_a,feat_b,feat_c,target"} $6=="train"{if($5=="positive") $5=1; else if($5=="negative") $5=0; print $1","$2","$3","$4","$5}' /home/user/data/raw_samples.csv > /home/user/data/train_ready.csv
cat /home/user/data/train_ready.csv
