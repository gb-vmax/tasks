#!/bin/bash
set -e
cd /home/user/restore_test

# Write the Makefile with a restore target
# IMPORTANT: The echo output must use Unicode right arrow U+2192 (→)
# Makefile recipe lines MUST be indented with a real tab character
cat > Makefile << 'MAKEEOF'
.PHONY: restore

restore:
	@for f in *.bak; do \
		base=$$(basename "$$f" .bak); \
		cp "$$f" "$${base}.restored"; \
		echo "Restored: $$f → $${base}.restored"; \
	done
MAKEEOF

make restore
