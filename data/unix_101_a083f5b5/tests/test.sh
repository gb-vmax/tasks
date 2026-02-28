#!/bin/bash
set -e
cd /home/user
tmpdir=$(mktemp -d)
cp archive.cpio "$tmpdir/"
cd "$tmpdir"
cpio -id < archive.cpio >/dev/null 2>&1
diff a.txt /home/user/a.txt && diff b.txt /home/user/b.txt && [ -f a.txt ] && [ -f b.txt ] && echo 1 > /logs/verifier/reward.txt || echo 0 > /logs/verifier/reward.txt
