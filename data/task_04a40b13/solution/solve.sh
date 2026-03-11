#!/bin/bash
set -e
cd /home/user

cat /home/user/translations/fr.po
grep -c '^msgstr ""$' /home/user/translations/fr.po
echo "Untranslated strings: 6" > /home/user/translations/untranslated_count.txt
sed -i 's/"X-Untranslated-Count: 0\\n"/"X-Untranslated-Count: 6\\n"/' /home/user/translations/fr.po
cat /home/user/translations/untranslated_count.txt && grep "X-Untranslated-Count" /home/user/translations/fr.po
