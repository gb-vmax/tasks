FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the pipeline_data directory structure
mkdir -p /home/user/pipeline_data/raw_inputs
mkdir -p /home/user/pipeline_data/processed
mkdir -p /home/user/pipeline_data/tmp_scratch
mkdir -p /home/user/pipeline_data/archives
mkdir -p /home/user/pipeline_data/logs

# raw_inputs: ~200K
dd if=/dev/zero of=/home/user/pipeline_data/raw_inputs/batch1.dat bs=1K count=100 2>/dev/null
dd if=/dev/zero of=/home/user/pipeline_data/raw_inputs/batch2.dat bs=1K count=100 2>/dev/null

# processed: ~500K
dd if=/dev/zero of=/home/user/pipeline_data/processed/output1.dat bs=1K count=250 2>/dev/null
dd if=/dev/zero of=/home/user/pipeline_data/processed/output2.dat bs=1K count=250 2>/dev/null

# tmp_scratch: ~50K
dd if=/dev/zero of=/home/user/pipeline_data/tmp_scratch/work.tmp bs=1K count=50 2>/dev/null

# archives: ~1M
dd if=/dev/zero of=/home/user/pipeline_data/archives/archive1.tar bs=1K count=512 2>/dev/null
dd if=/dev/zero of=/home/user/pipeline_data/archives/archive2.tar bs=1K count=512 2>/dev/null

# logs: ~20K
dd if=/dev/zero of=/home/user/pipeline_data/logs/pipeline.log bs=1K count=20 2>/dev/null

# Do NOT create disk_report.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
