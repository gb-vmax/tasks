FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

cat > /home/user/sshd_config << 'EOF'
# This is the sshd server system-wide configuration file.
Protocol 2
HostKey /etc/ssh/ssh_host_rsa_key
PermitRootLogin yes
MaxAuthTries 4
PubkeyAuthentication yes
PasswordAuthentication yes
PermitEmptyPasswords no
X11Forwarding yes
PrintMotd no
AcceptEnv LANG LC_*
Subsystem sftp /usr/lib/openssh/sftp-server
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
