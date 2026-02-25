#!/bin/bash
set -e
cd /home/user

awk -F',' '{
  status=$3; gsub(/^[[:space:]]+|[[:space:]]+$/, "", status);
  id=$1; gsub(/^[[:space:]]+|[[:space:]]+$/, "", id);
  if(status != "SUCCESS"){
    print id >> "/home/user/artifacts/failed-artifacts.txt";
    print "RECOVERED: [" id "]" >> "/home/user/artifacts/artifact-pipeline.log";
    print 1 >> "/tmp/failed_marker_awk_run";
  } else {
    print "PROCESSED: [" id "]" >> "/home/user/artifacts/artifact-pipeline.log";
  }
}
END{
  close("/home/user/artifacts/failed-artifacts.txt");
  close("/home/user/artifacts/artifact-pipeline.log");
  close("/tmp/failed_marker_awk_run");
}' /home/user/artifacts/build-output.txt; if [ -s /tmp/failed_marker_awk_run ]; then echo "One or more artifacts failed and are recorded."; fi; rm -f /tmp/failed_marker_awk_run
cat /home/user/artifacts/artifact-pipeline.log
cat /home/user/artifacts/failed-artifacts.txt
