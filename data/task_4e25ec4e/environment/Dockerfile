FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with
mkdir -p /home/user/workflows

cat > /home/user/workflows/base_workflow.yaml <<'EOF'
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Run tests
        run: echo "Running tests"
EOF

cat > /home/user/workflows/advanced_workflow.toml <<'EOF'
[job.test]
runs_on = "ubuntu-latest"
[[job.test.steps]]
name = "Run tests"
run = "echo 'Running tests'"
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
