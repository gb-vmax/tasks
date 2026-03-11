#!/bin/bash
set -e
cd /home/user

cat /home/user/ci/pipeline_timings.log
awk 'BEGIN{max=0; total=0} {total+=$2; if($2>max){max=$2; name=$1}} END{print "bottleneck: " name " (" max "s)"; print "total_duration: " total "s"}' /home/user/ci/pipeline_timings.log > /home/user/ci/bottleneck.txt
cat /home/user/ci/bottleneck.txt
