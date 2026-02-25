FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
install -d -m 755 /home/user/ml_data/raw_images
install -d -m 755 /home/user/ml_data/fetched

# Create cat1.jpg with exact required contents
echo -n "dummyimagecontent" > /home/user/ml_data/raw_images/cat1.jpg

# Create dog1.jpg (content not relevant, but file must exist)
touch /home/user/ml_data/raw_images/dog1.jpg

# Ensure fetched directory is empty (should already be, but just in case)
rm -f /home/user/ml_data/fetched/*

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
