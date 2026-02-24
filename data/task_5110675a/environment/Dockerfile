FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
set -e

apt-get update
apt-get install -y python3-pip make
pip3 install pytest

# Create user if not exists
if ! id user >/dev/null 2>&1; then
    useradd -m user
fi

# Ensure the restore_test directory exists and is owned by user
mkdir -p /home/user/restore_test
chown user:user /home/user/restore_test
chmod 755 /home/user/restore_test

# Create .bak files with correct contents and permissions
echo -n "DATA1" > /home/user/restore_test/file1.bak
echo -n "DATA2" > /home/user/restore_test/file2.bak
echo -n "DATA3" > /home/user/restore_test/file3.bak
chown user:user /home/user/restore_test/file1.bak /home/user/restore_test/file2.bak /home/user/restore_test/file3.bak
chmod 644 /home/user/restore_test/file1.bak /home/user/restore_test/file2.bak /home/user/restore_test/file3.bak
ENDPOST

WORKDIR /home/user
