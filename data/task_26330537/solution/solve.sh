#!/bin/bash
set -euo pipefail

# Create directory structure
mkdir -p /home/user/repos/binmgr

# Create artifact_client.sh script
cat > /home/user/repos/binmgr/artifact_client.sh << 'SCRIPT'
#!/bin/bash
echo "artifact-client running on PID $$"
sleep 120
SCRIPT
chmod +x /home/user/repos/binmgr/artifact_client.sh

# Clear process log
> /home/user/repos/binmgr/process_log.txt

# Launch 3 background instances, log PIDs, kill them, log termination
for i in 1 2 3; do
    /home/user/repos/binmgr/artifact_client.sh &
    PID=$!
    START_TS=$(date '+%Y-%m-%d %H:%M:%S')
    echo "PID: ${PID} | CMD: /home/user/repos/binmgr/artifact_client.sh | START: ${START_TS}" >> /home/user/repos/binmgr/process_log.txt
    kill "$PID" 2>/dev/null || true
    wait "$PID" 2>/dev/null || true
    END_TS=$(date '+%Y-%m-%d %H:%M:%S')
    echo "PID: ${PID} | STATUS: TERMINATED | END: ${END_TS}" >> /home/user/repos/binmgr/process_log.txt
done
