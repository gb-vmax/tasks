FROM ubuntu:22.04

RUN <<'ENDPOST'
apt-get update
    apt-get install -y python3-pip
    pip3 install pytest

    # Create the required directory structure
    mkdir -p /home/user/docs_project/final_drafts

    # Create markdown files with the specified content
    cat > /home/user/docs_project/final_drafts/chapter1.md <<'EOF'
# Chapter 1
Content of chapter 1.
EOF

    cat > /home/user/docs_project/final_drafts/chapter2.md <<'EOF'
# Chapter 2
Content of chapter 2.
EOF

    cat > /home/user/docs_project/final_drafts/chapter3.md <<'EOF'
# Chapter 3
Content of chapter 3.
EOF

    # Set permissions to ensure user-level access
    chown -R 1000:1000 /home/user/docs_project
ENDPOST

WORKDIR /home/user
