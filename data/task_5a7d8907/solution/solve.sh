#!/bin/bash
set -e
cd /home/user

find /home/user/l10n -type f -o -type l | sort
ls -la /home/user/l10n/active/
cd /home/user/l10n/active && rm pt_BR.po && ln -s ../versions/pt_BR_v2.po pt_BR.po && rm fr.po && ln -s ../versions/fr_v2.po fr.po && ln -s ../versions/ja_v1.po ja.po && ln -s ../versions/ko_v1.po ko.po
ls -la /home/user/l10n/active/
cd /home/user/l10n/active && for f in $(ls -1 | sort); do if [ -L "$f" ]; then echo "$f -> $(readlink $f)"; fi; done > MANIFEST.txt && cat MANIFEST.txt
echo "=== Symlinks ===" && ls -la /home/user/l10n/active/ && echo "=== MANIFEST.txt ===" && cat /home/user/l10n/active/MANIFEST.txt && echo "=== Line count ===" && wc -l /home/user/l10n/active/MANIFEST.txt
