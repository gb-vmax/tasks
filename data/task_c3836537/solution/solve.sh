#!/bin/bash
set -e
cd /home/user

cat /home/user/monitoring/hosts.txt
cat > /home/user/monitoring/check_uptime.sh << 'EOF'
#!/bin/bash

HOSTS_FILE="/home/user/monitoring/hosts.txt"
REPORT_FILE="/home/user/monitoring/uptime_report.txt"

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

hosts=()
statuses=()
up_count=0
down_count=0

while IFS= read -r line; do
    # Skip blank lines and lines starting with #
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    hosts+=("$line")
done < "$HOSTS_FILE"

for host in "${hosts[@]}"; do
    if ping -c 2 -W 3 "$host" > /dev/null 2>&1; then
        statuses+=("UP")
        ((up_count++))
    else
        statuses+=("DOWN")
        ((down_count++))
    fi
done

{
    echo "=== Uptime Report ==="
    echo "Timestamp: $TIMESTAMP"
    echo "Hosts checked: ${#hosts[@]}"
    echo ""
    echo "Status:"
    for i in "${!hosts[@]}"; do
        echo "  ${hosts[$i]}: ${statuses[$i]}"
    done
    echo ""
    echo "Summary:"
    echo "  UP:   $up_count"
    echo "  DOWN: $down_count"
} > "$REPORT_FILE"
EOF
chmod +x /home/user/monitoring/check_uptime.sh && /home/user/monitoring/check_uptime.sh
cat /home/user/monitoring/uptime_report.txt
ping -c 2 -W 3 localhost
which nc curl wget nmap 2>/dev/null; ls /usr/bin/ping* /bin/ping* 2>/dev/null
apt-get install -y iputils-ping 2>&1 | tail -5
apt-get install -y inetutils-ping 2>&1 | tail -5
ls /bin /usr/bin | grep -E "ping|nc|curl|wget|nmap|fping|hping"
(echo > /dev/tcp/localhost/22) 2>&1; echo "exit: $?"
ss -tlnp 2>/dev/null || netstat -tlnp 2>/dev/null || cat /proc/net/tcp
cat /etc/hosts
getent hosts localhost && getent hosts fake-host-one.internal; echo "exit: $?"
cat > /home/user/monitoring/check_uptime.sh << 'EOF'
#!/bin/bash

HOSTS_FILE="/home/user/monitoring/hosts.txt"
REPORT_FILE="/home/user/monitoring/uptime_report.txt"

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

hosts=()
statuses=()
up_count=0
down_count=0

check_host() {
    local host="$1"
    if command -v ping > /dev/null 2>&1; then
        ping -c 2 -W 3 "$host" > /dev/null 2>&1
        return $?
    else
        getent hosts "$host" > /dev/null 2>&1
        return $?
    fi
}

while IFS= read -r line; do
    # Skip blank lines and lines starting with #
    [[ -z "$line" || "$line" =~ ^# ]] && continue
    hosts+=("$line")
done < "$HOSTS_FILE"

for host in "${hosts[@]}"; do
    if check_host "$host"; then
        statuses+=("UP")
        ((up_count++))
    else
        statuses+=("DOWN")
        ((down_count++))
    fi
done

{
    echo "=== Uptime Report ==="
    echo "Timestamp: $TIMESTAMP"
    echo "Hosts checked: ${#hosts[@]}"
    echo ""
    echo "Status:"
    for i in "${!hosts[@]}"; do
        echo "  ${hosts[$i]}: ${statuses[$i]}"
    done
    echo ""
    echo "Summary:"
    echo "  UP:   $up_count"
    echo "  DOWN: $down_count"
} > "$REPORT_FILE"
EOF
chmod +x /home/user/monitoring/check_uptime.sh && /home/user/monitoring/check_uptime.sh
cat /home/user/monitoring/uptime_report.txt
