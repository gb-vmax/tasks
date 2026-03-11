FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create backup directory
mkdir -p /home/user/backup

# Create manifest file
cat > /home/user/backup/packages_manifest.txt << 'EOF'
requests==2.28.1
flask==2.2.0
numpy==1.24.0
click==8.1.3
Werkzeug==2.2.2
EOF

# Create the archive contents in a temp directory
TMPDIR=$(mktemp -d)
mkdir -p "$TMPDIR/site-packages/requests-2.28.1.dist-info"
mkdir -p "$TMPDIR/site-packages/flask-2.2.0.dist-info"
mkdir -p "$TMPDIR/site-packages/numpy-1.24.0.dist-info"
mkdir -p "$TMPDIR/site-packages/click-8.1.3.dist-info"
mkdir -p "$TMPDIR/site-packages/Werkzeug-2.2.2.dist-info"

cat > "$TMPDIR/site-packages/requests-2.28.1.dist-info/METADATA" << 'EOF'
Metadata-Version: 2.1
Name: requests
Version: 2.28.1
Summary: Python HTTP for Humans.
EOF

cat > "$TMPDIR/site-packages/flask-2.2.0.dist-info/METADATA" << 'EOF'
Metadata-Version: 2.1
Name: flask
Version: 2.2.0
Summary: A simple framework for building complex web applications.
EOF

cat > "$TMPDIR/site-packages/numpy-1.24.0.dist-info/METADATA" << 'EOF'
Metadata-Version: 2.1
Name: numpy
Version: 1.24.0
Summary: Fundamental package for array computing in Python.
EOF

cat > "$TMPDIR/site-packages/click-8.1.3.dist-info/METADATA" << 'EOF'
Metadata-Version: 2.1
Name: click
Version: 8.1.3
Summary: Composable command line interface toolkit.
EOF

cat > "$TMPDIR/site-packages/Werkzeug-2.2.2.dist-info/METADATA" << 'EOF'
Metadata-Version: 2.1
Name: Werkzeug
Version: 2.2.2
Summary: The comprehensive WSGI web application library.
EOF

# Create the tar.gz archive
cd "$TMPDIR"
tar -czf /home/user/backup/restore_archive.tar.gz site-packages/
cd /
rm -rf "$TMPDIR"

# Create restore target directory structure
mkdir -p /home/user/restore_target/site-packages/requests-2.28.1.dist-info
mkdir -p /home/user/restore_target/site-packages/flask-2.1.0.dist-info
mkdir -p /home/user/restore_target/site-packages/click-8.1.3.dist-info
mkdir -p /home/user/restore_target/site-packages/Werkzeug-2.2.2.dist-info
mkdir -p /home/user/restore_target/site-packages/itsdangerous-2.1.2.dist-info

cat > /home/user/restore_target/site-packages/requests-2.28.1.dist-info/METADATA << 'EOF'
Metadata-Version: 2.1
Name: requests
Version: 2.28.1
Summary: Python HTTP for Humans.
EOF

cat > /home/user/restore_target/site-packages/flask-2.1.0.dist-info/METADATA << 'EOF'
Metadata-Version: 2.1
Name: flask
Version: 2.1.0
Summary: A simple framework for building complex web applications.
EOF

cat > /home/user/restore_target/site-packages/click-8.1.3.dist-info/METADATA << 'EOF'
Metadata-Version: 2.1
Name: click
Version: 8.1.3
Summary: Composable command line interface toolkit.
EOF

cat > /home/user/restore_target/site-packages/Werkzeug-2.2.2.dist-info/METADATA << 'EOF'
Metadata-Version: 2.1
Name: Werkzeug
Version: 2.2.2
Summary: The comprehensive WSGI web application library.
EOF

cat > /home/user/restore_target/site-packages/itsdangerous-2.1.2.dist-info/METADATA << 'EOF'
Metadata-Version: 2.1
Name: itsdangerous
Version: 2.1.2
Summary: Safely pass data to untrusted environments and back.
EOF

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
