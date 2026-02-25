FROM ubuntu:22.04

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Create user and project directory
    useradd -m user
    mkdir -p /home/user/old_project
    chown -R user:user /home/user

    # Create main.py with the specified content
    cat << 'EOF' > /home/user/old_project/main.py
print("Project executed successfully!")
import utils
utils.helper()
EOF

    # Create utils.py with the specified content
    cat << 'EOF' > /home/user/old_project/utils.py
def helper():
    print("Helper function called.")
EOF

    # Set correct permissions
    chown user:user /home/user/old_project/main.py /home/user/old_project/utils.py
    chmod 644 /home/user/old_project/main.py /home/user/old_project/utils.py
ENDPOST

WORKDIR /home/user
