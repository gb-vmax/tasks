#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/audit
cat > /home/user/audit/gen_audit_entry.sh << 'EOF'
#!/bin/bash
export TZ=UTC
export LANG=en_US.UTF-8
TIMESTAMP=$(TZ=UTC date +"%Y-%m-%dT%H:%M:%SZ")
echo "${TIMESTAMP}|COMPLIANCE|INFO|Audit trail initialized|TZ=UTC|LANG=en_US.UTF-8" >> /home/user/audit/audit_trail.log
EOF
chmod +x /home/user/audit/gen_audit_entry.sh
/home/user/audit/gen_audit_entry.sh
cat /home/user/audit/audit_trail.log
