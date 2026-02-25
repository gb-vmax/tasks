FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/logs
cat > /home/user/logs/optim-solver.log <<'EOF'
[2024-06-03 10:01:15] INFO Solver started
[2024-06-03 10:01:19] WARNING Convergence slow
[2024-06-03 10:01:21] INFO Checking constraints
[2024-06-03 10:01:22] ERROR Constraint violation detected
[2024-06-03 10:01:23] INFO Retrying
[2024-06-03 10:01:26] WARNING Memory usage high
[2024-06-03 10:01:27] INFO Solver finished
EOF
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
