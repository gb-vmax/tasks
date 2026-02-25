FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
# Do NOT run the solution or create output files

# Create the report file with the exact required content
cat > /home/user/cloud_cost_report_Q2.txt <<EOF
Cloud cost savings for Q2: \$18,430
EOF

# Generate a new GPG key for Jane Finops with no passphrase
export GNUPGHOME="/home/user/.gnupg"
mkdir -p "$GNUPGHOME"
chmod 700 "$GNUPGHOME"
cat > /tmp/jane-gpg-batch <<EOF
%no-protection
Key-Type: default
Key-Length: 3072
Subkey-Type: default
Name-Real: Jane Finops
Name-Email: jane.finops@example.com
Expire-Date: 0
%commit
EOF
gpg --batch --generate-key /tmp/jane-gpg-batch
rm -f /tmp/jane-gpg-batch

# Create a detached signature for the report file with Jane's key
gpg --yes --batch --local-user "jane.finops@example.com" --output /home/user/cloud_cost_report_Q2.txt.sig --detach-sign /home/user/cloud_cost_report_Q2.txt

# Encrypt the report file to Jane's public key
gpg --yes --batch --recipient "jane.finops@example.com" --output /home/user/cloud_cost_report_Q2.txt.gpg --encrypt /home/user/cloud_cost_report_Q2.txt

# Verify the signature and write the verification log in the required format
# Get current system time in required format
now=$(date '+%Y-%m-%d %H:%M:%S')
verify_out=$(gpg --verify /home/user/cloud_cost_report_Q2.txt.sig /home/user/cloud_cost_report_Q2.txt 2>&1 || true)
if echo "$verify_out" | grep -q 'gpg: Good signature from "Jane Finops <jane.finops@example.com>"'; then
    status="GOOD"
else
    status="BAD"
fi
echo "[$now] Verification status: $status signature for cloud_cost_report_Q2.txt" > /home/user/cloud_cost_report_verification.log

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
