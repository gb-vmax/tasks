#!/bin/bash
set -e
cd /home/user

ls /home/user/backup/ && ls /home/user/restore_target/ 2>/dev/null || echo "restore_target not found"
cat /home/user/backup/packages_manifest.txt
ls /home/user/restore_target/site-packages/
for d in /home/user/restore_target/site-packages/*.dist-info; do echo "=== $d ==="; cat "$d/METADATA" 2>/dev/null | head -5; done
mkdir -p /home/user/restore_work && tar -xzf /home/user/backup/restore_archive.tar.gz -C /home/user/restore_work/
ls /home/user/restore_work/site-packages/
for d in /home/user/restore_work/site-packages/*.dist-info; do echo "=== $d ==="; cat "$d/METADATA" 2>/dev/null | head -5; done
python3 -c "
import os

def parse_metadata(path):
    name = version = None
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith('Name:') and not name:
                name = line.split(':',1)[1].strip()
            elif line.startswith('Version:') and not version:
                version = line.split(':',1)[1].strip()
            if name and version:
                break
    return name, version

def parse_dir(path):
    pkgs = {}
    for entry in os.listdir(path):
        if entry.endswith('.dist-info'):
            md = os.path.join(path, entry, 'METADATA')
            if os.path.isfile(md):
                n, v = parse_metadata(md)
                if n and v:
                    pkgs[n.lower()] = (n, v)
    return pkgs

arch = parse_dir('/home/user/restore_work/site-packages')
tgt = parse_dir('/home/user/restore_target/site-packages')

lines = []
ok = wrong = miss = 0
for key in sorted(arch.keys()):
    an, av = arch[key]
    if key in tgt:
        tn, tv = tgt[key]
        if av == tv:
            lines.append(f'{an}=={av} [OK]')
            ok += 1
        else:
            lines.append(f'{an}=={av} -> {tv} [WRONG_VERSION]')
            wrong += 1
    else:
        lines.append(f'{an}=={av} [MISSING]')
        miss += 1

extra_lines = []
extra = 0
for key in sorted(tgt.keys()):
    if key not in arch:
        tn, tv = tgt[key]
        extra_lines.append(f'{tn}=={tv} [EXTRA]')
        extra += 1

status = 'SUCCESS' if wrong == 0 and miss == 0 else 'INCOMPLETE'
total = len(arch)

report = '=== RESTORE VERIFICATION REPORT ===\n'
report += 'Archive: /home/user/backup/restore_archive.tar.gz\n'
report += 'Target: /home/user/restore_target/site-packages\n\n'
report += '--- PACKAGE STATUS ---\n'
report += '\n'.join(lines) + '\n\n'
report += '--- EXTRA PACKAGES IN TARGET ---\n'
report += ('\n'.join(extra_lines) if extra_lines else 'None') + '\n\n'
report += '--- SUMMARY ---\n'
report += f'Total packages in archive: {total}\n'
report += f'OK: {ok}\n'
report += f'WRONG_VERSION: {wrong}\n'
report += f'MISSING: {miss}\n'
report += f'EXTRA: {extra}\n'
report += f'Restore status: {status}\n'

with open('/home/user/restore_report.txt', 'w') as f:
    f.write(report)
print('Done')
"
cat /home/user/restore_report.txt
