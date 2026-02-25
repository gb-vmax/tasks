FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

# Install Python3 and pip
apt-get update
apt-get install -y python3 python3-pip

# Install pytest
pip3 install pytest

# Create user home and docs directories
mkdir -p /home/user/docs/guide
mkdir -p /home/user/docs/reference

# Create required markdown documentation files
echo "# Overview" > /home/user/docs/overview.md
echo "# Introduction" > /home/user/docs/guide/introduction.md
echo "# Getting Started" > /home/user/docs/guide/getting_started.md
echo "# FAQ" > /home/user/docs/faq.md
echo "# API Reference" > /home/user/docs/reference/api.md
echo "# Overview (Reference)" > /home/user/docs/reference/overview.md

# Ensure correct permissions: readable/writable/executable for user
chmod -R u+rwx /home/user/docs
chmod 755 /home/user/docs
chmod 755 /home/user/docs/guide
chmod 755 /home/user/docs/reference
ENDPOST

WORKDIR /home/user
