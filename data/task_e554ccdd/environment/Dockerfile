FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

BASE="/home/user/dashboards"

# Create directory structure
mkdir -p "$BASE/templates/infra"
mkdir -p "$BASE/templates/app"
mkdir -p "$BASE/templates/db"
mkdir -p "$BASE/active/production"
mkdir -p "$BASE/active/staging"
mkdir -p "$BASE/active/development"
mkdir -p "$BASE/archive"

# Create template files
echo -n '{"dashboard":"nodes","version":1}' > "$BASE/templates/infra/nodes_v1.json"
echo -n '{"dashboard":"nodes","version":2}' > "$BASE/templates/infra/nodes_v2.json"
echo -n '{"dashboard":"nodes","version":3}' > "$BASE/templates/infra/nodes_v3.json"

echo -n '{"dashboard":"latency","version":1}' > "$BASE/templates/app/latency_v1.json"
echo -n '{"dashboard":"latency","version":2}' > "$BASE/templates/app/latency_v2.json"

echo -n '{"dashboard":"requests","version":1}' > "$BASE/templates/app/requests_v1.json"
echo -n '{"dashboard":"requests","version":2}' > "$BASE/templates/app/requests_v2.json"
echo -n '{"dashboard":"requests","version":3}' > "$BASE/templates/app/requests_v3.json"

echo -n '{"dashboard":"queries","version":1}' > "$BASE/templates/db/queries_v1.json"
echo -n '{"dashboard":"queries","version":2}' > "$BASE/templates/db/queries_v2.json"

# Create production symlinks (initial/outdated state)
ln -s "../../templates/infra/nodes_v1.json" "$BASE/active/production/nodes.json"
ln -s "../../templates/app/latency_v2.json" "$BASE/active/production/latency.json"
ln -s "../../templates/app/requests_v2.json" "$BASE/active/production/requests.json"

# Create staging symlinks (initial state with outdated latency)
ln -s "../../templates/infra/nodes_v2.json" "$BASE/active/staging/nodes.json"
ln -s "../../templates/app/latency_v1.json" "$BASE/active/staging/latency.json"
ln -s "../../templates/app/requests_v3.json" "$BASE/active/staging/requests.json"

# active/development/ stays empty
# archive/ stays empty
# audit_report.txt must NOT exist

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
