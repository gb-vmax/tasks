FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create the utils directory
mkdir -p /home/user/utils

# Create the word_freq.py script (non-executable, mode 0644)
cat > /home/user/utils/word_freq.py << 'EOF'
#!/usr/bin/env python3
import sys
import string

def main():
    path = sys.argv[1]
    with open(path) as f:
        text = f.read()
    words = text.lower().split()
    cleaned = [w.strip(string.punctuation) for w in words]
    cleaned = [w for w in cleaned if w]
    freq = {}
    for w in cleaned:
        freq[w] = freq.get(w, 0) + 1
    for word in sorted(freq):
        print(f"{word}: {freq[word]}")
    print()
    print(f"total unique words: {len(freq)}")

main()
EOF

# Set permissions to 0644 (non-executable)
chmod 0644 /home/user/utils/word_freq.py

# Create the sample.txt file
cat > /home/user/utils/sample.txt << 'EOF'
The quick brown fox jumps over the lazy dog.
The dog barked at the fox, and the fox ran away.
EOF

# Do NOT create report.txt — that's the agent's task

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
