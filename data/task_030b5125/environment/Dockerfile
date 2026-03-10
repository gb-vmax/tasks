FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create artifacts directory
mkdir -p /home/user/deploy/artifacts

# Create the fake archive files with specific content
echo "auth-service version 2.1.4 fake archive content" > /home/user/deploy/artifacts/auth-service-2.1.4.tar.gz
echo "billing-service version 1.8.0 fake archive content" > /home/user/deploy/artifacts/billing-service-1.8.0.tar.gz
echo "gateway-service version 3.0.2 fake archive content" > /home/user/deploy/artifacts/gateway-service-3.0.2.tar.gz

# Generate the SHA256 checksums manifest in alphabetical order (bare filenames)
cd /home/user/deploy/artifacts
(
  sha256sum auth-service-2.1.4.tar.gz
  sha256sum billing-service-1.8.0.tar.gz
  sha256sum gateway-service-3.0.2.tar.gz
) > /home/user/deploy/checksums.sha256

# Ensure the file ends with a newline (sha256sum output already includes one per line)
# Verify it looks correct
cat /home/user/deploy/checksums.sha256

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
