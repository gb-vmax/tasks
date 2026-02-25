#!/bin/bash
set -e
cd /home/user

cd /home/user/localization && \
if [ ! -w fr.txt ]; then \
  touch fr.txt && chmod 664 fr.txt; \
fi && \
awk -F= '/=/{print $1}' en.txt | sort > .en_keys && \
awk -F= '/=/{print $1}' fr.txt 2>/dev/null | sort > .fr_keys && \
comm -23 .en_keys .fr_keys > .missing_keys && \
if [ -s .missing_keys ]; then \
  while read key; do echo "$key=" >> fr.txt; echo "Added missing translation: $key"; done < .missing_keys > update_log.txt; \
else \
  echo "No missing translations found." > update_log.txt; \
fi && \
rm -f .en_keys .fr_keys .missing_keys && \
chown user:user fr.txt update_log.txt
cat fr.txt && echo "---" && cat update_log.txt
