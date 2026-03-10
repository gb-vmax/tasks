FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the research directory
mkdir -p /home/user/research

# Create requirements.txt
cat > /home/user/research/requirements.txt << 'EOF'
numpy==1.26.4
pandas==2.2.1
EOF

# Create check_env.py
cat > /home/user/research/check_env.py << 'EOF'
import sys
import os

results = []

try:
    import numpy
    results.append("numpy: OK ({})".format(numpy.__version__))
except ImportError:
    results.append("numpy: MISSING")

try:
    import pandas
    results.append("pandas: OK ({})".format(pandas.__version__))
except ImportError:
    results.append("pandas: MISSING")

venv_path = "/home/user/research/venv"
using_venv = sys.prefix == venv_path
results.append("venv active: {}".format(using_venv))

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "env_status.txt")
with open(output_path, "w") as f:
    f.write("\n".join(results) + "\n")
EOF

# Do NOT create venv or env_status.txt — those are for the agent to create

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
