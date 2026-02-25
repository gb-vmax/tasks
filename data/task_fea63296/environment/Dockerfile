FROM ubuntu:22.04

ENV PATH=/home/user/.local/bin:$PATH

RUN <<'ENDPOST'
set -e

# Create user and home directory
useradd -m -d /home/user user

# Install Python3 and pip
apt-get update
apt-get install -y python3 python3-pip

# Install pytest for testing
pip3 install pytest

# Create initial state directories and files as described

# 1. /home/user/android_old with two files
mkdir -p /home/user/android_old
dd if=/dev/urandom of=/home/user/android_old/app-release.apk bs=997 count=1 status=none
dd if=/dev/urandom of=/home/user/android_old/proguard-rules.txt bs=415 count=1 status=none

# 2. /home/user/some/other/path/ios_old with two files
mkdir -p /home/user/some/other/path/ios_old
dd if=/dev/urandom of=/home/user/some/other/path/ios_old/Runner.app bs=2234 count=1 status=none
dd if=/dev/urandom of=/home/user/some/other/path/ios_old/launch.log bs=78 count=1 status=none

# 3. Set ownership and permissions
chown -R user:user /home/user
chmod 700 /home/user
chmod 700 /home/user/android_old
chmod 600 /home/user/android_old/app-release.apk
chmod 600 /home/user/android_old/proguard-rules.txt
chmod 700 /home/user/some
chmod 700 /home/user/some/other
chmod 700 /home/user/some/other/path
chmod 700 /home/user/some/other/path/ios_old
chmod 600 /home/user/some/other/path/ios_old/Runner.app
chmod 600 /home/user/some/other/path/ios_old/launch.log
ENDPOST

WORKDIR /home/user
