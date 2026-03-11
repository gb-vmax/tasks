#!/bin/bash
set -e
cd /home/user

cat /home/user/registry/image_manifest.tsv
awk -F'\t' '($3 == "ubuntu:18.04" || $3 == "debian:stretch") {print $1"\t"$2"\t"$3"\t"$4}' /home/user/registry/image_manifest.tsv | sort -t$'\t' -k1,1 | awk -F'\t' 'BEGIN{count=0} {print "[DEPRECATED] "$1" ("$2") uses "$3" \xe2\x80\x94 pushed by "$4; count++} END{print ""; print "Total deprecated images: "count}' > /home/user/registry/deprecated_report.txt
cat /home/user/registry/deprecated_report.txt
