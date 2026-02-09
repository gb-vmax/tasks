#!/bin/bash
set -euo pipefail
cd /testbed

# The fix is to reverse the bug patch
# This undoes the bug that was introduced
git apply --reverse /solution/fix.patch || patch -R -p1 < /solution/fix.patch

echo "Applied fix (reversed bug patch)"
