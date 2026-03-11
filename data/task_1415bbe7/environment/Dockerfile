FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the artifacts directory and files
mkdir -p /home/user/artifacts/v2.4.0

printf 'ELFBINARY_APP_AMD64_v2.4.0\n' > /home/user/artifacts/v2.4.0/app-linux-amd64
printf 'ELFBINARY_APP_ARM64_v2.4.0\n' > /home/user/artifacts/v2.4.0/app-linux-arm64
printf 'MACHOBINARY_APP_AMD64_v2.4.0\n' > /home/user/artifacts/v2.4.0/app-darwin-amd64
printf 'app-linux-amd64: abc123\napp-linux-arm64: def456\napp-darwin-amd64: ghi789\n' > /home/user/artifacts/v2.4.0/checksums.txt

# Do NOT create /home/user/backups/ or any output files — the agent will do that

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
