FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    # Install Python3, pip, sqlite3, and pytest
    apt-get update
    apt-get install -y python3 python3-pip sqlite3
    pip3 install pytest

    # Create the user and home directory
    useradd -m -s /bin/bash user

    # Create /home/user/projects directory with correct ownership
    mkdir -p /home/user/projects
    chown user:user /home/user/projects

    # Create the SQLite database with the required schema and data
    su - user -c "sqlite3 /home/user/projects/tasks.db <<'EOF'
CREATE TABLE files (
    id INTEGER PRIMARY KEY,
    filename TEXT NOT NULL,
    project TEXT NOT NULL,
    date_added TEXT NOT NULL
);
INSERT INTO files (id, filename, project, date_added) VALUES
    (1, 'main.py', 'alpha', '2024-05-01'),
    (2, 'README.md', 'alpha', '2024-05-02'),
    (3, 'utils.py', 'beta', '2024-05-03');
EOF"

    # Ensure correct permissions and ownership for the database file
    chown user:user /home/user/projects/tasks.db
    chmod 0644 /home/user/projects/tasks.db
ENDPOST

WORKDIR /home/user
