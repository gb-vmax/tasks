FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin

RUN <<'ENDPOST'
set -e

    # Create user and home directory if not present
    if ! id user 2>/dev/null; then
        useradd -m -s /bin/bash user
    fi

    # Ensure /home/user exists and set proper permissions
    mkdir -p /home/user
    chown user:user /home/user
    chmod 755 /home/user

    # Create the raw_data.csv file with the exact required content
    cat > /home/user/raw_data.csv <<'EOF'
id,name,age,department,salary,hire_date
1,Jane Doe,34,Engineering,92000,2018-06-21
2,John Smith,29,Marketing,67000,2019-12-01
3,Amy Adams,41,Engineering,105000,2016-03-17
4,Mark Lee,52,Human Resources,98000,2010-09-06
5,Leila Chan,37,Finance,88000,2015-11-23
EOF

    # Set ownership and permissions so the agent (user) can read/write as needed
    chown user:user /home/user/raw_data.csv
    chmod 644 /home/user/raw_data.csv

    # Install pip and pytest (python3-pip and pytest via pip)
    apt-get update
    apt-get install -y python3-pip python3-setuptools python3-wheel
    pip3 install --no-cache-dir pytest
ENDPOST

WORKDIR /home/user
