FROM endless-deps-87d163a8074d:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the project directory with only run_workflow.py
mkdir -p /home/user/automation_project

cat > /home/user/automation_project/run_workflow.py << 'EOF'
import requests
import schedule
from dotenv import load_dotenv

print("Workflow environment OK")
EOF

# Ensure correct ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
