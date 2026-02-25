FROM ubuntu:22.04

RUN <<'ENDPOST'
set -eux

    # Install Python 2 and pip for Python 2
    apt-get update
    apt-get install -y python2 python2-dev wget

    # Symlink python2 to /usr/bin/python for compatibility if needed
    if ! command -v python2 >/dev/null; then
        ln -s /usr/bin/python2 /usr/bin/python2
    fi

    # Install pip for Python 2
    wget https://bootstrap.pypa.io/pip/2.7/get-pip.py -O /tmp/get-pip.py
    python2 /tmp/get-pip.py
    rm /tmp/get-pip.py

    # Install pytest (for Python 3, for test harness)
    apt-get install -y python3-pip
    python3 -m pip install --no-cache-dir pytest

    # Create user and legacy_app directory
    useradd -m user || true
    mkdir -p /home/user/legacy_app
    chown -R user:user /home/user/legacy_app

    # Create a sample Python 2 script as /home/user/legacy_app/collect_info.py
    cat > /home/user/legacy_app/collect_info.py <<'EOF'
#!/usr/bin/env python2
import sys
import socket
import platform
import time
import subprocess

def get_uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            days = int(uptime_seconds // (24*3600))
            hours = int((uptime_seconds % (24*3600)) // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            return "%d days, %d:%02d" % (days, hours, minutes)
    except Exception:
        # Fallback to uptime command output
        try:
            output = subprocess.check_output(['uptime'], universal_newlines=True)
            return output.strip()
        except Exception:
            return "Unavailable"

def get_os_version():
    try:
        with open('/etc/os-release', 'r') as f:
            for line in f:
                if line.startswith('PRETTY_NAME='):
                    return line.strip().split('=',1)[1].strip('"')
    except Exception:
        pass
    # Fallback
    return platform.platform()

def main():
    print("System Diagnostics Report - %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Hostname: %s" % socket.gethostname())
    print("OS Version: %s" % get_os_version())
    print("Uptime: %s" % get_uptime())
    print("Additional diagnostic info can go here.")

if __name__ == '__main__':
    main()
EOF

    chmod 755 /home/user/legacy_app/collect_info.py
    chown user:user /home/user/legacy_app/collect_info.py
ENDPOST

WORKDIR /home/user
