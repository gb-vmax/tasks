FROM ubuntu:22.04

ENV PATH=/usr/local/bin:/usr/bin:/bin:$PATH

RUN <<'ENDPOST'
set -e

    # Install Python3, pip, and jq (for jq extraction)
    apt-get update
    apt-get install -y python3 python3-pip jq

    # Install pytest for testing
    pip3 install --no-cache-dir pytest

    # Create the user home and required directories
    mkdir -p /home/user/manifests
    mkdir -p /home/user/schemas

    # Write the manifest file with exact contents
    cat >/home/user/manifests/nginx-deployment.json <<'EOF'
{
  "apiVersion": "apps/v1",
  "kind": "Deployment",
  "metadata": {
    "name": "nginx-deployment"
  },
  "spec": {
    "replicas": 3,
    "selector": {
      "matchLabels": {
        "app": "nginx"
      }
    },
    "template": {
      "metadata": {
        "labels": {
          "app": "nginx"
        }
      },
      "spec": {
        "containers": [
          {
            "name": "nginx",
            "image": "nginx:1.21.1",
            "ports": [
              {
                "containerPort": 80
              }
            ]
          }
        ]
      }
    }
  }
}
EOF

    # Write the schema file with exact contents
    cat >/home/user/schemas/deployment-schema.json <<'EOF'
{
  "type": "object",
  "properties": {
    "apiVersion": {
      "type": "string",
      "enum": ["apps/v1"]
    },
    "kind": {
      "type": "string",
      "enum": ["Deployment"]
    },
    "metadata": {
      "type": "object",
      "properties": {
        "name": { "type": "string" }
      },
      "required": ["name"]
    },
    "spec": {
      "type": "object",
      "properties": {
        "replicas": { "type": "integer" },
        "template": {
          "type": "object",
          "properties": {
            "spec": {
              "type": "object",
              "properties": {
                "containers": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "image": { "type": "string" }
                    },
                    "required": ["image"]
                  }
                }
              },
              "required": ["containers"]
            }
          },
          "required": ["spec"]
        }
      },
      "required": ["replicas", "template"]
    }
  },
  "required": ["apiVersion", "kind", "metadata", "spec"]
}
EOF

    # Set the permissions so that user can read/write as needed
    chown -R 1000:1000 /home/user
    chmod -R u+rwX /home/user
ENDPOST

WORKDIR /home/user
