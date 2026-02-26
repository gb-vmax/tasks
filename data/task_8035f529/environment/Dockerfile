FROM endless-base:latest

ENV PATH=/usr/local/bin:/usr/bin:/bin

RUN <<'ENDPOST'
set -e

    # Install Python3, pip, and pytest
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install --no-cache-dir pytest

    # Create user home directory and set permissions
    mkdir -p /home/user
    chown -R nobody:nogroup /home/user
    chmod 755 /home/user

    # Create /home/user/cloud_costs.csv with LF line endings and specified content
    cat > /home/user/cloud_costs.csv << 'EOF'
service_name,usage_hours,cost_usd
Compute-Engine,720,105.60
Cloud-SQL,500,175.00
Object-Storage,1200,80.00
Cloud-Firewall,400,40.00
BigQuery,90,54.00
Kubernetes-Engine,300,90.00
Content-Delivery,150,20.00
EOF

    # Ensure LF line endings
    sed -i 's/\r$//' /home/user/cloud_costs.csv

    # Create /home/user/services_to_optimize.json with specified content
    cat > /home/user/services_to_optimize.json << 'EOF'
[
    "Cloud-SQL",
    "Kubernetes-Engine",
    "Compute-Engine",
    "BigQuery"
]
EOF

    # Set permissions so user can read/write these files, but not optimized_costs_report.csv yet
    chown nobody:nogroup /home/user/cloud_costs.csv /home/user/services_to_optimize.json
    chmod 644 /home/user/cloud_costs.csv /home/user/services_to_optimize.json
ENDPOST

WORKDIR /home/user
