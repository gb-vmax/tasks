FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
cat > /home/user/sample_config.txt <<'EOF'
ServerName=ExempleServeur
Location=Europe
ContactName=René Durand
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
