FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the experiment directory and files
mkdir -p /home/user/datasets/experiment_42

cat > /home/user/datasets/experiment_42/measurements_a.csv << 'EOF'
time,value
0,1.2
1,3.4
2,5.6
EOF

cat > /home/user/datasets/experiment_42/measurements_b.csv << 'EOF'
time,value
0,7.8
1,9.0
2,1.1
EOF

cat > /home/user/datasets/experiment_42/results_final.csv << 'EOF'
sample,mean,stddev
A,2.07,1.83
B,5.97,0.75
EOF

cat > /home/user/datasets/experiment_42/lab_notes.txt << 'EOF'
Experiment 42 notes
Run on 2024-01-10
Conditions: temperature 22C
EOF

cat > /home/user/datasets/experiment_42/run.log << 'EOF'
[INFO] Starting experiment
[INFO] Data collection complete
[WARN] Sensor 3 offline during run
EOF

# Do NOT create /home/user/backups — the agent will create it

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
