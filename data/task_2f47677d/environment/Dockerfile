FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/iot/configs

cat > /home/user/iot/configs/device_A1.ini << 'EOF'
[device]
id = A1
model = SensorPro-200
firmware_version = 1.4
enabled = true

[network]
protocol = mqtt
ip_address = 192.168.1.10
port = 1883

[sensor]
type = temperature
sample_rate_hz = 10
calibration_offset = -0.5

[power]
battery_pct = 85
sleep_mode = light
EOF

cat > /home/user/iot/configs/device_B3.ini << 'EOF'
[device]
id = B3
model = SensorPro-200
firmware_version = 2.1
enabled = true

[network]
protocol = mqtt
ip_address = 192.168.1.11
port = 1883

[sensor]
type = humidity
sample_rate_hz = 5
calibration_offset = 0.2

[power]
battery_pct = 60
sleep_mode = deep
EOF

cat > /home/user/iot/configs/device_C7.ini << 'EOF'
[device]
id = C7
model = EdgeNode-100
firmware_version = 1.9
enabled = false

[network]
protocol = coap
ip_address = 10.0.0.5
port = 5683

[sensor]
type = pressure
sample_rate_hz = 20
calibration_offset = 1.0

[power]
battery_pct = 45
sleep_mode = off
EOF

cat > /home/user/iot/configs/device_D2.ini << 'EOF'
[device]
id = D2
model = MicroSense-50
firmware_version = 1.1
enabled = true

[network]
protocol = http
ip_address = 172.16.0.3
port = 8080

[sensor]
type = temperature
sample_rate_hz = 15
calibration_offset = 0.8

[power]
battery_pct = 15
sleep_mode = deep
EOF

cat > /home/user/iot/configs/device_E5.ini << 'EOF'
[device]
id = E5
model = SensorPro-400
firmware_version = 1.7
enabled = true

[network]
protocol = mqtt
ip_address = 192.168.2.20
port = 1883

[sensor]
type = vibration
sample_rate_hz = 50
calibration_offset = -1.2

[power]
battery_pct = 72
sleep_mode = light
EOF

cat > /home/user/iot/configs/device_F9.ini << 'EOF'
[device]
id = F9
model = EdgeNode-100
firmware_version = 2.0
enabled = true

[network]
protocol = coap
ip_address = 10.0.0.9
port = 5683

[sensor]
type = humidity
sample_rate_hz = 8
calibration_offset = 0.3

[power]
battery_pct = 90
sleep_mode = off
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
