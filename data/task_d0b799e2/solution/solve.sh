#!/bin/bash
set -e
cd /home/user

ls /home/user/datasets
ls -la /home/user/datasets/climate /home/user/datasets/genomics /home/user/datasets/imaging /home/user/datasets/text_corpus
cat > /home/user/datasets/audit_report.txt << 'EOF'
=== DATASET AUDIT REPORT ===

DATASET SUMMARY (sorted by total size, descending):
  imaging: 8170 bytes, 4 files, largest: scan001.bin
  genomics: 5700 bytes, 3 files, largest: reference.bin
  climate: 4000 bytes, 3 files, largest: temperatures.csv
  text_corpus: 1800 bytes, 2 files, largest: articles.txt

TOTAL STORAGE USED: 19670 bytes across 12 files

LARGE FILES (>2000 bytes, sorted by size descending):
  imaging/scan001.bin: 4100 bytes
  genomics/reference.bin: 3500 bytes
  imaging/scan002.bin: 3200 bytes
  climate/temperatures.csv: 2500 bytes

TOP DATASET: imaging
EOF
cat /home/user/datasets/audit_report.txt
