FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/artifacts

cat > /home/user/artifacts/inventory.psv << 'EOF'
artifact_name|version|arch|checksum_sha256|size_bytes|upload_date
libssl.so.1.1|1.1.1n|x86_64|a3f1c29d8e4b56f0123456789abcdef0123456789abcdef0123456789abcdef01|2097152|2024-01-15
libcurl.so.4|7.88.1|x86_64|b4e2d30a9f5c67e1234567890bcdef1234567890bcdef1234567890bcdef1234|1048576|2024-01-22
nginx-1.24.0|1.24.0|aarch64|c5f3e41baf6d78f2345678901cdef2345678901cdef2345678901cdef234567|5242880|2024-02-03
python3.11|3.11.4|x86_64|d6a4f52cbg7e89034567890123ef3456789012ef3456789012ef3456789012ef|31457280|2024-02-18
redis-server|7.0.11|aarch64|e7b5063dch8f90145678901234f04567890123f04567890123f04567890123f0|8388608|2024-03-07
EOF

cat > /home/user/artifacts/repo_ids.txt << 'EOF'
repo_id
R001
R002
R003
R004
R005
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
