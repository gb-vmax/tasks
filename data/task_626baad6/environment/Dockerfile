FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
install -d -m 700 /home/user/data
cat > /home/user/data/training_text.txt <<EOF
cat
dog
cat
bird
EOF
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
