#!/bin/bash
EXPECTED='\/home\/user\/project\n├── README.md\n├── src\n│   ├── main.c\n│   └── utils.c\n└── test\n    └── test_main.c'
OUTPUT=$(tree -L 2 /home/user/project | sed 's/\x1b\[[0-9;]*m//g')
echo "$OUTPUT" | grep -q "README.md" && \
  echo "$OUTPUT" | grep -q "src" && \
  echo "$OUTPUT" | grep -q "main.c" && \
  echo "$OUTPUT" | grep -q "utils.c" && \
  echo "$OUTPUT" | grep -q "test" && \
  echo "$OUTPUT" | grep -q "test_main.c" && \
  [ $(echo "$OUTPUT" | grep -c "project") -ge 1 ] && \
  [ $(echo "$OUTPUT" | grep -c "src") -ge 1 ] && \
  [ $(echo "$OUTPUT" | grep -c "test") -ge 1 ] && \
  [ $(echo "$OUTPUT" | grep -c "README.md") -eq 1 ] && {
  echo 1 > /logs/verifier/reward.txt
} || {
  echo 0 > /logs/verifier/reward.txt
}
