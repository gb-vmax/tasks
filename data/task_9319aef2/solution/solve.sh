#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/research/datasets/raw/images /home/user/research/datasets/raw/tabular /home/user/research/datasets/processed/train /home/user/research/datasets/processed/val /home/user/research/datasets/processed/test /home/user/research/datasets/archive
cat > /home/user/research/datasets/INDEX.txt << 'EOF'
DATASET REGISTRY
================

raw/images       - unprocessed image files
raw/tabular      - unprocessed CSV and tabular data
processed/train  - training split
processed/val    - validation split
processed/test   - test split
archive          - deprecated or backed-up datasets
EOF
chmod 500 /home/user/research/datasets/archive
ls -ld /home/user/research/datasets/archive && echo "---" && ls -lR /home/user/research/datasets && echo "---" && cat /home/user/research/datasets/INDEX.txt
