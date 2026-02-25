#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/data/organized/cats /home/user/data/organized/dogs /home/user/data/organized/birds
sh -c 'num_cats=$(find /home/user/data/raw_images -maxdepth 1 -type f -name "cats_*.jpg" | wc -l); mv /home/user/data/raw_images/cats_*.jpg /home/user/data/organized/cats/ 2>/dev/null; echo $num_cats > /home/user/data/organized/._num_cats'
sh -c 'num_dogs=$(find /home/user/data/raw_images -maxdepth 1 -type f -name "dogs_*.jpg" | wc -l); mv /home/user/data/raw_images/dogs_*.jpg /home/user/data/organized/dogs/ 2>/dev/null; echo $num_dogs > /home/user/data/organized/._num_dogs'
sh -c 'num_birds=$(find /home/user/data/raw_images -maxdepth 1 -type f -name "birds_*.jpg" | wc -l); mv /home/user/data/raw_images/birds_*.jpg /home/user/data/organized/birds/ 2>/dev/null; echo $num_birds > /home/user/data/organized/._num_birds'
mkdir -p /home/user/data/archive && mv /home/user/data/old /home/user/data/archive/
rm -rf /home/user/data/temp
sh -c 'num_cats=$(cat /home/user/data/organized/._num_cats); num_dogs=$(cat /home/user/data/organized/._num_dogs); num_birds=$(cat /home/user/data/organized/._num_birds); printf -- "---\nDatasets Organized: %s cats images, %s dogs images, %s birds images\nOld files archived to: /home/user/data/archive/old\nTemporary files deleted: /home/user/data/temp\nDirectories created under /home/user/data/organized:\n- cats\n- dogs\n- birds\n---\n" "$num_cats" "$num_dogs" "$num_birds" > /home/user/data/organization_log.txt'
cat /home/user/data/organization_log.txt
