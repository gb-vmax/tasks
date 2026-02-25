FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python3 and pip
    apt-get update
    apt-get install -y python3 python3-pip

    # Install pytest
    pip3 install pytest

    # Create user and home directory
    useradd -m user
    mkdir -p /home/user
    chown user:user /home/user

    # Create solvers directory and two executables
    mkdir -p /home/user/solvers
    cat << 'EOF' > /home/user/solvers/solverX
#!/bin/bash
# Dummy solverX: output solution text for the input file
inputfile="$1"
problem=$(basename "$inputfile" .dat)
echo "solution of solverX on $problem"
EOF

    cat << 'EOF' > /home/user/solvers/solverY
#!/bin/bash
# Dummy solverY: output solution text for the input file
inputfile="$1"
problem=$(basename "$inputfile" .dat)
echo "solution of solverY on $problem"
EOF

    chmod 755 /home/user/solvers/solverX
    chmod 755 /home/user/solvers/solverY
    chown user:user /home/user/solvers/solverX /home/user/solvers/solverY

    # Create inputs directory and two .dat files
    mkdir -p /home/user/inputs
    echo "max 2x+3y subject to x+y<=4; x,y>=0" > /home/user/inputs/problemA.dat
    echo "min x^2+y^2 subject to x+y=5; x,y>=0" > /home/user/inputs/problemB.dat
    chown -R user:user /home/user/inputs

    # Ensure permissions for solvers dir
    chown -R user:user /home/user/solvers

    # Do not create or touch /home/user/outputs/ per instructions
ENDPOST

WORKDIR /home/user
