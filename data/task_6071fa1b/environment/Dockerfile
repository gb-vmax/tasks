FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the ml_project directory
mkdir -p /home/user/ml_project

# Create the training data CSV file (no header, 4 columns per row)
cat > /home/user/ml_project/training_data.csv << 'EOF'
1,2.30,1.50,cat
2,0.50,4.80,bird
3,4.40,6.20,dog
4,1.20,0.30,cat
5,3.20,1.10,bird
6,0.80,1.50,dog
7,5.60,3.90,cat
8,1.80,2.20,bird
9,2.10,3.70,dog
10,3.40,1.90,cat
11,1.50,4.10,bird
12,4.10,5.30,dog
13,2.90,2.60,cat
14,0.90,3.30,dog
15,3.80,2.80,cat
EOF

# Do NOT create class_stats.txt — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
