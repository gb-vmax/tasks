FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Ensure user and home directory exist
    useradd -m user || true

    # Create the /home/user/data directory and employees.csv file with correct content and permissions
    mkdir -p /home/user/data
    cat <<EOF > /home/user/data/employees.csv
id,name,department,salary
1,Alice,Engineering,95000
2,Bob,Sales,70000
3,Charlie,Engineering,99000
4,David,HR,60000
EOF
    chown -R user:user /home/user/data
    chmod 755 /home/user/data
    chmod 644 /home/user/data/employees.csv
ENDPOST

WORKDIR /home/user
