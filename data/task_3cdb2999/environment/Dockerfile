FROM endless-deps-87d163a8074d:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directories
mkdir -p /home/user/data
mkdir -p /home/user/scripts

# Create the raw CSV file
cat > /home/user/data/sales_raw.csv << 'EOF'
order_id,region,revenue
1001,North,4500.75
1002,  South  ,3200.00
1003,East,
1004,West,1800.50
1005,  North  ,-200.00
1006,South,9100.99
1007,East,
1008,West,4400.10
1009,  South  ,7750.25
1010,North,-50.00
EOF

# Create the cleaning script
cat > /home/user/scripts/clean_sales.py << 'EOF'
import pandas as pd

df = pd.read_csv('/home/user/data/sales_raw.csv')
df = df.dropna(subset=['revenue'])
df = df[df['revenue'] >= 0]
df['region'] = df['region'].str.strip()
df['revenue'] = df['revenue'].astype(int)
df.to_csv('/home/user/data/sales_clean.csv', index=False)
EOF

# Set correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
