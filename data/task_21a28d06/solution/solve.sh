#!/bin/bash
set -e
cd /home/user

ls -la /home/user/i18n/active/
ln -sf ../locales/en_US/messages.po /home/user/i18n/active/english.po && ln -sf ../locales/pt_BR/messages.po /home/user/i18n/active/portuguese.po
printf 'english.po -> ../locales/en_US/messages.po\nfrench.po -> ../locales/fr_FR/messages.po\nportugese.po -> ../locales/pt_BR/messages.po\n' > /home/user/i18n/symlink_report.txt
printf 'english.po -> ../locales/en_US/messages.po\nfrench.po -> ../locales/fr_FR/messages.po\nportuguese.po -> ../locales/pt_BR/messages.po\n' > /home/user/i18n/symlink_report.txt
ls -la /home/user/i18n/active/ && echo "---" && cat /home/user/i18n/symlink_report.txt
