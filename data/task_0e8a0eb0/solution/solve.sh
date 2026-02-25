#!/bin/bash
set -e
cd /home/user

python3 -c "import configparser; c = configparser.ConfigParser(dict_type=dict); c.read('/home/user/artifact_manager/repos.ini'); with open('/home/user/artifact_manager/enabled_repos.log', 'w') as f: [f.write(f'{s}: {c[s][\"base_url\"]}\n') for s in c.sections() if c[s].get('enabled','').lower() == 'yes']"
python3 -c "import configparser; c = configparser.ConfigParser(dict_type=dict); c.read('/home/user/artifact_manager/repos.ini'); f = open('/home/user/artifact_manager/enabled_repos.log', 'w'); [f.write('%s: %s\n' % (s, c[s]['base_url'])) for s in c.sections() if c[s].get('enabled','').lower() == 'yes']; f.close()"
cat /home/user/artifact_manager/enabled_repos.log
