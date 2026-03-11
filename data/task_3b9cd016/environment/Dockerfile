FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/tickets

cat > /home/user/tickets/open_tickets.tsv << 'EOF'
ticket_id	assigned_agent	priority	created_date	category	status	customer_email
TKT-001	alice	high	2024-05-01	billing	open	john.doe@example.com
TKT-002	bob	low	2024-05-02	network	pending	sara.smith@example.com
TKT-003	alice	medium	2024-05-03	hardware	open	mike.jones@example.com
TKT-004	carol	high	2024-05-04	software	open	linda.wu@example.com
TKT-005	bob	low	2024-05-05	billing	resolved	raj.patel@example.com
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
