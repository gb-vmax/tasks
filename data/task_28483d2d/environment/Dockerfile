FROM endless-base:latest

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3 python3-pip
    pip3 install pytest

    # Create the user and project directories
    mkdir -p /home/user/project

    # Create the CSV file with the required contents
    cat > /home/user/project/access_report.csv <<EOF
username,filename,permission
alice,secret.txt,write
bob,log.txt,execute
carol,data.txt,read
dave,audit.log,read
EOF

    # Set permissions so non-root users can read/write as needed
    chmod 755 /home/user
    chmod 755 /home/user/project
    chmod 644 /home/user/project/access_report.csv
ENDPOST

WORKDIR /home/user
