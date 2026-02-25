#!/bin/bash
set -e
cd /home/user

awk -F',' 'BEGIN{OFS=","} NR==1{print; next} $1=="greeting"{$3="Salut"} $1=="farewell"{$3="Au revoir"} {print}' /home/user/translations.csv > /home/user/translations.csv.tmp && mv /home/user/translations.csv.tmp /home/user/translations.csv
python3 -c "import csv,json; f=open('/home/user/translations.csv'); r=csv.DictReader(f); d={row['en']:row['fr'] for row in r}; json.dump(d,open('/home/user/translations_fr.json','w'),ensure_ascii=False,indent=2); f.close()"
cat /home/user/translations_fr.json
