#!/bin/bash
set -e
cd /home/user

cat /home/user/data/sales.csv
python3 -m venv /home/user/analyst_env
sudo apt install python3.10-venv -y
python3 --version && apt-cache search python3.*venv
apt-cache search venv
python3 -m venv --without-pip /home/user/analyst_env
curl -sS https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py && /home/user/analyst_env/bin/python3 /tmp/get-pip.py
wget -q https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py && /home/user/analyst_env/bin/python3 /tmp/get-pip.py
python3 -c "import urllib.request; urllib.request.urlretrieve('https://bootstrap.pypa.io/get-pip.py', '/tmp/get-pip.py')"
/home/user/analyst_env/bin/python3 /tmp/get-pip.py
/home/user/analyst_env/bin/pip install pandas
/home/user/analyst_env/bin/pip install pandas --timeout 300
cat > /home/user/data/analyze.py << 'EOF'
import pandas as pd

df = pd.read_csv('/home/user/data/sales.csv')

total_revenue = round(df['revenue'].sum(), 2)
average_revenue = round(df['revenue'].mean(), 2)

region_counts = df['region'].value_counts()
max_count = region_counts.max()
top_regions = region_counts[region_counts == max_count].index.tolist()
top_region = sorted(top_regions)[0]

total_transactions = len(df)

report = f"""Sales Report
============
Total Revenue: {total_revenue:.2f}
Average Revenue: {average_revenue:.2f}
Top Region: {top_region}
Total Transactions: {total_transactions}
"""

with open('/home/user/data/report.txt', 'w') as f:
    f.write(report)
EOF
/home/user/analyst_env/bin/python3 /home/user/data/analyze.py
cat /home/user/data/report.txt
cat -A /home/user/data/report.txt
