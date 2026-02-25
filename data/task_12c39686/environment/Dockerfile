FROM ubuntu:22.04

ENV PATH=/home/user/.local/bin:$PATH

RUN <<'ENDPOST'
set -eux

# Install pip and pytest
apt-get update
apt-get install -y python3-pip
pip3 install --no-cache-dir pytest

# Create user and set up directories with correct permissions
useradd -m -d /home/user user || true
mkdir -p /home/user/app_profile/results
mkdir -p /home/user/remote_server/backup/results

# Create cpu.prof in source
dd if=/dev/zero of=/home/user/app_profile/results/cpu.prof bs=1 count=24576
# Set mtime to 2024-06-15T14:25:36Z (POSIX: 1718451936)
touch -m -d '2024-06-15T14:25:36Z' /home/user/app_profile/results/cpu.prof

# Create mem.prof in source and target
dd if=/dev/zero of=/home/user/app_profile/results/mem.prof bs=1 count=16832
touch -m -d '2024-06-15T14:21:00Z' /home/user/app_profile/results/mem.prof

dd if=/dev/zero of=/home/user/remote_server/backup/results/mem.prof bs=1 count=16832
touch -m -d '2024-06-15T14:21:00Z' /home/user/remote_server/backup/results/mem.prof

# Create old.prof in target
dd if=/dev/zero of=/home/user/remote_server/backup/results/old.prof bs=1 count=42000
touch -m -d '2024-06-10T09:00:00Z' /home/user/remote_server/backup/results/old.prof

# Set permissions: allow user to read/write/create in all relevant directories
chown -R user:user /home/user/app_profile
chown -R user:user /home/user/remote_server
chmod -R 755 /home/user/app_profile
chmod -R 755 /home/user/remote_server
ENDPOST

WORKDIR /home/user
