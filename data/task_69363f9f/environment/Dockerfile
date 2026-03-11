FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/api_data

# Create users.tsv
cat > /home/user/api_data/users.tsv << 'EOF'
created_at	user_id	email	full_name	status	department
2023-01-15	U001	alice@example.com	Alice Marsh	active	engineering
2023-02-20	U002	bob@example.com	Bob Chen	inactive	marketing
2023-03-10	U003	carol@example.com	Carol Singh	active	sales
2023-04-05	U004	dan@example.com	Dan Okafor	suspended	engineering
2023-05-18	U005	eve@example.com	Eve Torres	active	hr
EOF

# Create scores.tsv
cat > /home/user/api_data/scores.tsv << 'EOF'
user_id	login_count	engagement_score	last_active
U001	142	87	2024-11-01
U002	23	34	2024-09-15
U003	98	76	2024-10-30
U004	5	12	2024-07-04
U005	211	95	2024-11-03
EOF

# Create regions.tsv
cat > /home/user/api_data/regions.tsv << 'EOF'
user_id	country	city	timezone
U001	USA	New York	America/New_York
U002	Canada	Toronto	America/Toronto
U003	UK	London	Europe/London
U004	Nigeria	Lagos	Africa/Lagos
U005	Mexico	Mexico City	America/Mexico_City
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
