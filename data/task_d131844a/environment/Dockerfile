FROM ubuntu:22.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN <<'ENDPOST'
set -e

    # Install Python3 and pip, then pytest
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Create project directory structure
    mkdir -p /home/user/projects/resmon/reports
    mkdir -p /home/user/projects/resmon/resmon

    # Set permissions so user can write
    chmod -R 755 /home/user
    chmod -R 755 /home/user/projects
    chmod -R 755 /home/user/projects/resmon
    chmod -R 755 /home/user/projects/resmon/reports
    chmod -R 755 /home/user/projects/resmon/resmon

    # Create CHANGELOG.md with initial content
    cat > /home/user/projects/resmon/CHANGELOG.md <<EOF
## [1.4.2] - 2024-06-01
- Improved resource usage reporting accuracy.
EOF

    # Create usage report CSV
    cat > /home/user/projects/resmon/reports/usage_2024-06-01.csv <<EOF
resource,cpu_usage,mem_usage
web01,45,78
db01,67,85
api01,55,72
EOF

    # Create version.txt with initial version
    echo "1.4.2" > /home/user/projects/resmon/resmon/version.txt

    # Set permissions so user can modify all files
    chmod 644 /home/user/projects/resmon/CHANGELOG.md
    chmod 644 /home/user/projects/resmon/reports/usage_2024-06-01.csv
    chmod 644 /home/user/projects/resmon/resmon/version.txt
ENDPOST

WORKDIR /home/user
