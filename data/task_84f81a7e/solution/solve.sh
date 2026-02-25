#!/bin/bash
set -e
cd /home/user

jq '. + {"logout_message": "You have been logged out successfully."}' /home/user/localization/en.json > /home/user/localization/en.json.tmp && mv /home/user/localization/en.json.tmp /home/user/localization/en.json
python3 -c "import json; p='/home/user/localization/en.json'; d=json.load(open(p)); d['logout_message']='You have been logged out successfully.'; json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)"
python3 -c "import json; p='/home/user/localization/fr.json'; d=json.load(open(p)); d['logout_message']='Vous avez été déconnecté avec succès.'; json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)"
python3 -c "import json; p='/home/user/localization/de.json'; d=json.load(open(p)); d['logout_message']='Sie wurden erfolgreich abgemeldet.'; json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)"
python3 -c "import json; out = ''; files = {'en':'/home/user/localization/en.json', 'fr':'/home/user/localization/fr.json', 'de':'/home/user/localization/de.json'}; \
for k, f in files.items(): \
    with open(f) as fp: d = json.load(fp); \
    exists = 'logout_message' in d; \
    val = d['logout_message'] if exists else ''; \
    out += f'{k}:\n  exists: {str(exists).lower()}\n  value: \"{val}\"\n'; \
open('/home/user/localization/update_verification.log','w').write(out)"
echo -n "" > /home/user/localization/update_verification.log
python3 -c "import json; d=json.load(open('/home/user/localization/en.json')); print('en:'); print('  exists: true' if 'logout_message' in d else '  exists: false'); print(f'  value: \"{d.get(\"logout_message\",\"\")}\"')" >> /home/user/localization/update_verification.log
python3 -c "import json; d=json.load(open('/home/user/localization/fr.json')); print('fr:'); print('  exists: true' if 'logout_message' in d else '  exists: false'); print(f'  value: \"{d.get(\"logout_message\",\"\")}\"')" >> /home/user/localization/update_verification.log
python3 -c "import json; d=json.load(open('/home/user/localization/de.json')); print('de:'); print('  exists: true' if 'logout_message' in d else '  exists: false'); print(f'  value: \"{d.get(\"logout_message\",\"\")}\"')" >> /home/user/localization/update_verification.log
cat /home/user/localization/update_verification.log
