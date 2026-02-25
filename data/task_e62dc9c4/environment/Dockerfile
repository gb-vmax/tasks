FROM ubuntu:22.04

RUN <<'ENDPOST'
# Create user and home directory
useradd -m user
mkdir -p /home/user/mlops_artifacts

# Create world-writable files and directory with correct permissions and ownership
touch /home/user/mlops_artifacts/results.csv
touch /home/user/mlops_artifacts/model.pt
chmod 777 /home/user/mlops_artifacts
chmod 666 /home/user/mlops_artifacts/results.csv
chmod 666 /home/user/mlops_artifacts/model.pt
chown -R user:user /home/user

# Install pytest (for Python 3)
apt-get update
apt-get install -y python3-pip
pip3 install pytest
ENDPOST

WORKDIR /home/user
