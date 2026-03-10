FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

STAGING="/home/user/iot_staging"

# Create directory structure
mkdir -p "$STAGING/devices/sensor_a"
mkdir -p "$STAGING/devices/sensor_b"
mkdir -p "$STAGING/devices/gateway"
mkdir -p "$STAGING/shared"

# Create sensor_a files
printf '[sensor_a]\ntype=temperature\ninterval=30\n' > "$STAGING/devices/sensor_a/device.conf"
printf 'FWBIN_SENSOR_A_V2\n' > "$STAGING/devices/sensor_a/firmware_v2.bin"
printf 'OLDFIRMWARE\n' > "$STAGING/devices/sensor_a/old_firmware.bak"
printf 'tmp data\n' > "$STAGING/devices/sensor_a/build_temp.tmp"

# Create sensor_b files
printf '[sensor_b]\ntype=humidity\ninterval=60\n' > "$STAGING/devices/sensor_b/device.conf"
printf 'FWBIN_SENSOR_B_V2\n' > "$STAGING/devices/sensor_b/firmware_v2.bin"
printf 'cal tmp\n' > "$STAGING/devices/sensor_b/calibration.tmp"

# Create gateway files
printf '[gateway]\nport=8883\ntls=true\n' > "$STAGING/devices/gateway/gateway.conf"
printf 'FWBIN_GATEWAY\n' > "$STAGING/devices/gateway/gateway.bin"
printf 'old gateway\n' > "$STAGING/devices/gateway/gateway_old.bak"

# Create shared files
printf '[base]\nversion=2.1\nregion=us-east\n' > "$STAGING/shared/base.conf"
printf 'FWBIN_LOADER\n' > "$STAGING/shared/loader.bin"

# Create root-level tmp file
printf 'scratch\n' > "$STAGING/scratch.tmp"

# Set all files to 644
find "$STAGING" -type f -exec chmod 644 {} \;

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
