#!/bin/bash
set -e
cd /home/user

cat /home/user/services/api-gateway/config.env
python3 -c "
src = '/home/user/services/api-gateway/config.env'
out = '/home/user/services/api-gateway/config.compliant.env'
audit_path = '/home/user/services/api-gateway/audit.log'

banned_keys = {'DEBUG', 'DEV_MODE', 'LEGACY_AUTH_TOKEN'}
secret_substrings = ('SECRET', 'PASSWORD', 'TOKEN')

banned_removed = 0
secrets_redacted = 0
entries = []

with open(src) as f:
    for line in f:
        line = line.rstrip('\n')
        if not line.strip() or line.startswith('#'):
            continue
        if '=' not in line:
            continue
        key, value = line.split('=', 1)
        if key in banned_keys:
            banned_removed += 1
            continue
        if any(s in key for s in secret_substrings):
            value = '***REDACTED***'
            secrets_redacted += 1
        entries.append((key, value))

entries.sort(key=lambda x: x[0])
lines_written = len(entries)

with open(out, 'w') as f:
    f.write('# compliant-env-v1 policy=strict\n')
    f.write('\n')
    for key, value in entries:
        f.write(key + '=' + value + '\n')

with open(audit_path, 'w') as f:
    f.write('AUDIT: config.env policy enforcement\n')
    f.write('banned_removed: ' + str(banned_removed) + '\n')
    f.write('secrets_redacted: ' + str(secrets_redacted) + '\n')
    f.write('lines_written: ' + str(lines_written) + '\n')

print('Done. banned_removed=%d secrets_redacted=%d lines_written=%d' % (banned_removed, secrets_redacted, lines_written))
"
cat /home/user/services/api-gateway/config.compliant.env && echo "---" && cat /home/user/services/api-gateway/audit.log
