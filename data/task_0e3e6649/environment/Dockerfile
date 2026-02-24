FROM ubuntu:22.04

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3-pip
    pip3 install pytest

    # Create /home/user directory if it doesn't exist
    mkdir -p /home/user

    # Create the app_profile.csv file with the required contents and correct permissions
    cat > /home/user/app_profile.csv << 'EOF'
ProcessID,Process,User,Threads,CPU%,MemoryMB
1023,chrome,alice,14,32.5,450
1057,firefox,bob,8,42.1,305
1092,code,carol,10,15.7,210
1107,slack,dan,6,21.0,190
EOF

    # Ensure proper permissions for /home/user and the file
    chmod 755 /home/user
    chmod 644 /home/user/app_profile.csv
ENDPOST

WORKDIR /home/user
