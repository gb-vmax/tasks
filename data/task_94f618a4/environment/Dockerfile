FROM endless-base:latest

RUN <<'ENDPOST'
set -eux

# Install Python 3, venv, and pip
apt-get update
apt-get install -y python3 python3-venv python3-pip

# Create user and home directory if not present
useradd -m -s /bin/bash user || true
chown -R user:user /home/user

# Install pytest system-wide for testing
python3 -m pip install --upgrade pip
python3 -m pip install pytest

# As user, set up pyutils directory, virtualenv, install packages, and create package_list.txt
su - user -c '
    set -eux
    mkdir -p /home/user/pyutils
    cd /home/user/pyutils

    # Create virtual environment
    python3 -m venv venv

    # Activate venv and install only the required packages
    ./venv/bin/pip install --upgrade pip
    ./venv/bin/pip install requests==2.31.0 pytz==2024.1

    # Generate package_list.txt with only direct dependencies, sorted alphabetically
    echo -e "pytz==2024.1\nrequests==2.31.0" > package_list.txt
'

# Ensure ownership and permissions
chown -R user:user /home/user/pyutils
ENDPOST

WORKDIR /home/user
