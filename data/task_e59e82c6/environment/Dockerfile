FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    apt-get update
    apt-get install -y python3-pip
    pip3 install pytest

    # Create user and home directory if not already present
    if ! id user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Ensure directory structure exists
    mkdir -p /home/user/opt_solver/configs

    # Set up initial solver.conf
    cat > /home/user/opt_solver/configs/solver.conf <<EOF
# Solver configuration
max_iterations = 1000
tolerance = 1e-6
method = conjugate_gradient
EOF

    # Set up initial deploy.log
    mkdir -p /home/user/opt_solver
    echo "[2024-04-01 12:05:13] Initial deployment completed." > /home/user/opt_solver/deploy.log

    # Set permissions so 'user' can read/write
    chown -R user:user /home/user/opt_solver
    chmod -R u+rwX /home/user/opt_solver
ENDPOST

WORKDIR /home/user
