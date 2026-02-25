#!/bin/bash
set -e
cd /home/user

cat <<'EOF' > /home/user/scripts/prepare_data.sh
#!/bin/bash
while IFS= read -r line || [ -n "$line" ]; do
    trimmed=$(echo "$line" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
    echo "$trimmed" | tr '[:upper:]' '[:lower:]'
done < /home/user/data/raw_text.txt > /home/user/data/prepared_text.txt
EOF
chmod +x /home/user/scripts/prepare_data.sh && /home/user/scripts/prepare_data.sh
ls -l /home/user/data/ && cat /home/user/data/prepared_text.txt
