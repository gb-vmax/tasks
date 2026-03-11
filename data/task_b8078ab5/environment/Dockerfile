FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the initial .bashrc with the expected content
cat > /home/user/.bashrc << 'EOF'
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# User specific aliases and functions
alias ll='ls -la'
alias grep='grep --color=auto'

PATH=$PATH:$HOME/.local/bin:$HOME/bin
export PATH
EOF

# Ensure env_check.txt does NOT exist
rm -f /home/user/env_check.txt

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
