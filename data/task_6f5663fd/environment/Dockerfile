FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python3-pip and pytest
    apt-get update
    apt-get install -y python3-pip
    pip3 install pytest

    # Create user and home directory if not already present
    useradd -m -d /home/user user || true
    mkdir -p /home/user

    # Create required directories
    mkdir -p /home/user/data
    mkdir -p /home/user/scripts

    # Create /home/user/data/raw_text.txt with exact contents
    cat > /home/user/data/raw_text.txt << 'EOF'
The Quick brown Fox
  jumps Over the Lazy Dog


HELLO WORLD
  data science is Awesome

EOF

    # Create /home/user/scripts/prepare_data.sh with correct permissions
    cat > /home/user/scripts/prepare_data.sh << 'EOF'
#!/bin/bash
input="/home/user/data/raw_text.txt"
output="/home/user/data/prepared_text.txt"
while IFS= read -r line || [ -n "$line" ]; do
    trimmed="$(echo "$line" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
    echo "${trimmed,,}" >> "$output"
done < "$input"
EOF
    chmod 755 /home/user/scripts/prepare_data.sh

    # Set ownership so non-root user can write/read
    chown -R user:user /home/user
ENDPOST

WORKDIR /home/user
