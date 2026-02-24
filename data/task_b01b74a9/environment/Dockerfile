FROM ubuntu:22.04

ENV PATH=/home/user/.local/bin:$PATH

RUN <<'ENDPOST'
set -e

# Create user and set up home directory
useradd -m -s /bin/bash user

# Install pip and pytest
apt-get update
apt-get install -y python3-pip
pip3 install pytest

# Create required directories
mkdir -p /home/user/microservices/auth
mkdir -p /home/user/microservices/payment

# Create and populate auth.log
printf '[2024-06-01 09:00:00] User login successful.\n' > /home/user/microservices/auth/auth.log

# Create and populate payment.log
printf '[2024-06-01 09:05:22] Payment processed for order #1278.\n' > /home/user/microservices/payment/payment.log

# Set ownership and permissions for user:user
chown -R user:user /home/user/microservices
chmod 755 /home/user /home/user/microservices /home/user/microservices/auth /home/user/microservices/payment
chmod 644 /home/user/microservices/auth/auth.log
chmod 644 /home/user/microservices/payment/payment.log
ENDPOST

WORKDIR /home/user
