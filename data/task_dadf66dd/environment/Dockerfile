FROM ubuntu:22.04

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create the user and data directories
    mkdir -p /home/user/data

    # Create the input CSV file with the specified content
    cat <<EOF > /home/user/data/dirty_data.csv
id,value,label
1,12.5,A
2,,B
3,not_a_number,C
4,6.8,D
5,7.2,E
EOF

    # Set permissions so user can read/write in /home/user and /home/user/data
    chmod -R 0777 /home/user
ENDPOST

WORKDIR /home/user
