FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create directory structure
mkdir -p /home/user/iot_deploy/configs
mkdir -p /home/user/iot_deploy/services

# Create startup.sh (will be set to 0777 - world-writable = UNSAFE)
cat > /home/user/iot_deploy/startup.sh << 'EOF'
#!/bin/bash
# Device startup script
# password=ignored_because_comment

DEVICE_ID=sensor-042
api_key=AKIAIOSFODNN7EXAMPLE
update_server=http://updates.internal.example.com/firmware
telnet_fallback=disabled

echo "Starting device $DEVICE_ID"
/usr/bin/mosquitto_sub -h broker.local -t devices/#
EOF
chmod 0777 /home/user/iot_deploy/startup.sh

# Create configs/device.conf (0644 - not world-writable = OK)
cat > /home/user/iot_deploy/configs/device.conf << 'EOF'
# Device configuration file
device_name=edge-node-01
firmware_version=2.4.1
# secret=this_is_a_comment_ignore_me
password=admin123
log_level=info
management_protocol=telnet
backup_url=ftp://backup.internal.example.com/configs
EOF
chmod 0644 /home/user/iot_deploy/configs/device.conf

# Create configs/mqtt.conf (0666 - world-writable = UNSAFE)
cat > /home/user/iot_deploy/configs/mqtt.conf << 'EOF'
# MQTT broker configuration
broker_host=mqtt.internal.example.com
broker_port=1883
token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
# token=old_token_do_not_use
tls_enabled=false
allow_anonymous=true
EOF
chmod 0666 /home/user/iot_deploy/configs/mqtt.conf

# Create services/watchdog.service (0644 - not world-writable = OK)
cat > /home/user/iot_deploy/services/watchdog.service << 'EOF'
[Unit]
Description=IoT Watchdog Service

[Service]
ExecStart=/usr/bin/watchdog --config /etc/watchdog.conf
secret=watchdog_secret_key_9x2k
Restart=always

[Install]
WantedBy=multi-user.target
EOF
chmod 0644 /home/user/iot_deploy/services/watchdog.service

# Set ownership
chown -R user:user /home/user
EOF
ENDSETUP

WORKDIR /home/user
