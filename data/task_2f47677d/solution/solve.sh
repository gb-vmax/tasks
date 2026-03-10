#!/bin/bash
set -e
cd /home/user

ls /home/user/iot/configs/
cat /home/user/iot/configs/device_A1.ini
cat /home/user/iot/configs/device_B3.ini
cat /home/user/iot/configs/device_C7.ini
cat /home/user/iot/configs/device_D2.ini
cat /home/user/iot/configs/device_E5.ini
cat /home/user/iot/configs/device_F9.ini
cat << 'EOF' > /home/user/iot/deployment_manifest.txt
=== IoT Deployment Manifest ===
Generated for: edge-cluster-07
Total devices scanned: 6
Eligible for deployment: 2
Ineligible (skipped): 4

--- ELIGIBLE DEVICES ---
[A1]
  Model:              SensorPro-200
  Current Firmware:   1.4
  Network:            mqtt://192.168.1.10:1883
  Sensor Type:        temperature
  Sample Rate:        10 Hz
  Calibration Offset: -0.5
  Battery:            85%
  Sleep Mode:         light

[E5]
  Model:              SensorPro-400
  Current Firmware:   1.7
  Network:            mqtt://192.168.2.20:1883
  Sensor Type:        vibration
  Sample Rate:        50 Hz
  Calibration Offset: -1.2
  Battery:            72%
  Sleep Mode:         light

--- INELIGIBLE DEVICES ---
[B3] SKIP: firmware current (2.1)
[C7] SKIP: disabled
[D2] SKIP: low battery (15%)
[F9] SKIP: firmware current (2.0)

--- SENSOR STATISTICS (eligible devices) ---
Sensor types present: temperature, vibration
Average sample rate: 30.00 Hz
Highest calibration offset: -0.5
Lowest calibration offset: -1.2
EOF
cat /home/user/iot/deployment_manifest.txt
xxd /home/user/iot/deployment_manifest.txt | tail -5
od -c /home/user/iot/deployment_manifest.txt | tail -5
