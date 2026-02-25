FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

apt-get update
apt-get install -y python3 python3-pip sqlite3

pip3 install --no-cache-dir pytest

# Create user and ML data directory
useradd -m user || true
mkdir -p /home/user/ml_data
chown user:user /home/user/ml_data
chmod 700 /home/user/ml_data

# Create old_training_data.db with required schema and content
su - user -c "sqlite3 /home/user/ml_data/old_training_data.db \"CREATE TABLE train_samples (id INTEGER, sentence TEXT, label INTEGER);\
INSERT INTO train_samples (id, sentence, label) VALUES \
(1, 'I love bananas.', 0),\
(2, 'Hello, world!', 1),\
(3, 'The sky is blue.', 0);\""
ENDPOST

WORKDIR /home/user
