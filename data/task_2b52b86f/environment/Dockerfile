FROM endless-base:latest

RUN <<'ENDPOST'
set -eux

# Install python3 and pip, then pytest
apt-get update
apt-get install -y python3 python3-pip
pip3 install --no-cache-dir pytest

# Create user and home directory if not present
useradd -m user || true

# Set up directories
mkdir -p /home/user/storage_audit/subdir1
mkdir -p /home/user/storage_audit/subdir2

# Create /home/user/storage_audit/subdir1/largefile1.bin (15MB, no 'password')
dd if=/dev/urandom of=/home/user/storage_audit/subdir1/largefile1.bin bs=1M count=15 status=none

# Create /home/user/storage_audit/subdir2/largefile2.txt (22MB, 'password' on line 53)
# Make 52 lines of filler, then line 53 with 'password', then pad to 22MB
tmpfile=/home/user/storage_audit/subdir2/largefile2.txt
(
    for i in $(seq 1 52); do echo "This is filler line $i"; done
    echo "This file contains the password: hunter2"
) > "$tmpfile"
# Fill to 22MB (append zeros)
truncate -s 22M "$tmpfile"

# Create /home/user/storage_audit/subdir2/largefile3.dat (11MB, 'PASSWORD' on line 1)
echo 'PASSWORD = "secretphrase"' > /home/user/storage_audit/subdir2/largefile3.dat
# Pad with nulls to 11MB
truncate -s 11M /home/user/storage_audit/subdir2/largefile3.dat

# Create /home/user/storage_audit/smallfile.txt (2KB, no 'password')
head -c 2048 </dev/urandom > /home/user/storage_audit/smallfile.txt

# Create /home/user/storage_audit/unrelatedfile.log (500 bytes, no 'password')
head -c 500 </dev/urandom > /home/user/storage_audit/unrelatedfile.log

# Set ownership and permissions so user can read/write
chown -R user:user /home/user/storage_audit
chmod -R u+rwX,go+rX /home/user/storage_audit
ENDPOST

WORKDIR /home/user
