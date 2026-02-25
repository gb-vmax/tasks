FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python 2 and pip for pytest
    apt-get update
    apt-get install -y python2 python2-dev python3-pip

    # Install pytest (using pip3 so it is available for test runner)
    pip3 install pytest

    # Create user and set up home directory structure
    useradd -m user
    mkdir -p /home/user/legacy_tools
    mkdir -p /home/user/legacy_data
    mkdir -p /home/user/legacy_run/reports

    # Set ownership to user for all created directories and files
    chown -R user:user /home/user

    # Set permissions for directories
    chmod 700 /home/user/legacy_tools
    chmod 700 /home/user/legacy_run/reports
    chmod 700 /home/user/legacy_run
    chmod 700 /home/user/legacy_data

    # Create the legacy cleanup script with correct content and permissions
    cat > /home/user/legacy_tools/cleanup_temp_files.py << 'EOF'
#!/usr/bin/env python2

import os

def main():
    data_dir = '/home/user/legacy_data'
    files = os.listdir(data_dir)
    deleted = []
    for f in files:
        if f.endswith('.tmp'):
            try:
                os.remove(os.path.join(data_dir, f))
                deleted.append(f)
            except:
                pass
    print("Cleanup Summary:")
    print("Deleted files:")
    for fname in sorted(deleted):
        print("- {}".format(fname))
    print("Operation completed successfully.")

if __name__ == "__main__":
    main()
EOF

    chown user:user /home/user/legacy_tools/cleanup_temp_files.py
    chmod 700 /home/user/legacy_tools/cleanup_temp_files.py

    # Create the three .tmp files with correct permissions and content
    echo "tmp file 1" > /home/user/legacy_data/temp1.tmp
    echo "tmp file 2" > /home/user/legacy_data/temp2.tmp
    echo "tmp file 3" > /home/user/legacy_data/temp3.tmp
    chown user:user /home/user/legacy_data/temp1.tmp
    chown user:user /home/user/legacy_data/temp2.tmp
    chown user:user /home/user/legacy_data/temp3.tmp
    chmod 600 /home/user/legacy_data/temp1.tmp
    chmod 600 /home/user/legacy_data/temp2.tmp
    chmod 600 /home/user/legacy_data/temp3.tmp

    # Create the two non-tmp files with correct permissions and content
    echo "important data" > /home/user/legacy_data/keepme.txt
    echo "log file data" > /home/user/legacy_data/archive.log
    chown user:user /home/user/legacy_data/keepme.txt
    chown user:user /home/user/legacy_data/archive.log
    chmod 600 /home/user/legacy_data/keepme.txt
    chmod 600 /home/user/legacy_data/archive.log
ENDPOST

WORKDIR /home/user
