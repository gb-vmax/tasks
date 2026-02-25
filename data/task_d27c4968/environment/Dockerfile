FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

    # Create user and home directory if not exists
    if ! id -u user >/dev/null 2>&1; then
        useradd -m -s /bin/bash user
    fi

    # Install Python3, pip, jq, and other tools
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip jq

    # Install pytest and jsonschema (for schema validation in test dependencies)
    pip3 install --no-cache-dir pytest jsonschema

    # Prepare /home/user directory and files
    mkdir -p /home/user
    chown user:user /home/user

    # Write artifacts.schema.json
    cat > /home/user/artifacts.schema.json <<'EOF'
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "array",
  "items": {
    "type": "object",
    "required": ["artifact_id", "type", "created_at", "size_kb", "location"],
    "properties": {
      "artifact_id": { "type": "string" },
      "type": { "type": "string", "enum": ["checkpoint", "log", "plot"] },
      "created_at": { "type": "string", "format": "date-time" },
      "size_kb": { "type": "integer" },
      "location": { "type": "string" }
    }
  }
}
EOF

    # Write artifacts.json
    cat > /home/user/artifacts.json <<'EOF'
[
  {
    "artifact_id": "model_v1_ckpt",
    "type": "checkpoint",
    "created_at": "2023-10-01T12:05:00Z",
    "size_kb": 15280,
    "location": "/mnt/artifacts/model_v1/ckpt"
  },
  {
    "artifact_id": "train_logs",
    "type": "log",
    "created_at": "2023-10-01T12:07:23Z",
    "size_kb": 120,
    "location": "/mnt/artifacts/model_v1/train.log"
  },
  {
    "artifact_id": "learning_curve_plot",
    "type": "plot",
    "created_at": "2023-10-01T12:08:34Z",
    "size_kb": 32,
    "location": "/mnt/artifacts/model_v1/lc.png"
  },
  {
    "artifact_id": "model_v2_ckpt",
    "type": "checkpoint",
    "created_at": "2023-12-16T15:01:00Z",
    "size_kb": 24012,
    "location": "/mnt/artifacts/model_v2/ckpt"
  }
]
EOF

    # Set permissions so user can read/write their own files and home
    chown user:user /home/user/artifacts.schema.json
    chown user:user /home/user/artifacts.json
    chmod 644 /home/user/artifacts.schema.json /home/user/artifacts.json
    chmod 755 /home/user
ENDPOST

WORKDIR /home/user
