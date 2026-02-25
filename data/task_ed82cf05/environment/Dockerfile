FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    apt-get update
    apt-get install -y --no-install-recommends \
        git \
        python3-pip

    pip3 install pytest

    # Create user and home directory
    useradd -m -d /home/user user || true

    # Set up the target-repo directory
    mkdir -p /home/user/target-repo
    cd /home/user/target-repo

    # Initialize as a git repository
    git init

    # Create the .gitmodules file with the required contents
    cat > /home/user/target-repo/.gitmodules <<EOF
[submodule "vuln-lib"]
        path = libs/vuln-lib
        url = https://github.com/example/vuln-lib.git
[submodule "useful-util"]
        path = utils/useful-util
        url = https://github.com/example/useful-util.git
EOF

    # Set proper permissions
    chown -R user:user /home/user
ENDPOST

WORKDIR /home/user
