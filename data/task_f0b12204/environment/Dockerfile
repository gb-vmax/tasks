FROM endless-deps-c84d384f2a25:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/backups

cat > /home/user/backups/manifest.json << 'EOF'
{
  "backups": [
    {
      "id": "bkp-001",
      "filename": "db_full_20240301.tar.gz",
      "size_bytes": 1048576,
      "checksum": "a3f5c2e1d4b6789012345678abcdef01234567890abcdef1234567890abcdef12",
      "status": "complete"
    },
    {
      "id": "bkp-002",
      "filename": "db_full_20240302.tar.gz",
      "size_bytes": 0,
      "checksum": "b1c2d3e4f5a6789012345678abcdef01234567890abcdef1234567890abcdef34",
      "status": "complete"
    },
    {
      "id": "bkp-003",
      "filename": "db_full_20240303.tar.gz",
      "size_bytes": 2097152,
      "checksum": null,
      "status": "complete"
    },
    {
      "id": "bkp-004",
      "filename": "db_full_20240304.tar.gz",
      "size_bytes": 3145728,
      "checksum": "c4d5e6f7a8b9012345678901abcdef01234567890abcdef1234567890abcdef56",
      "status": "partial"
    },
    {
      "id": "bkp-005",
      "filename": "db_full_20240305.tar.gz",
      "size_bytes": 4194304,
      "checksum": "d6e7f8a9b0c1234567890123abcdef01234567890abcdef1234567890abcdef78",
      "status": "complete"
    },
    {
      "id": "bkp-006",
      "filename": "db_incremental_20240306.tar.gz",
      "size_bytes": 512000,
      "checksum": "e8f9a0b1c2d3456789012345abcdef01234567890abcdef1234567890abcdef90",
      "status": "complete"
    },
    {
      "id": "bkp-007",
      "filename": "db_incremental_20240307.tar.gz",
      "size_bytes": 0,
      "checksum": null,
      "status": "partial"
    }
  ]
}
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
