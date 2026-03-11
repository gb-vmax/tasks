FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create datastore directory structure
mkdir -p /home/user/datastore/projects/alpha
mkdir -p /home/user/datastore/projects/beta
mkdir -p /home/user/datastore/projects/shared
mkdir -p /home/user/datastore/media/images
mkdir -p /home/user/datastore/media/videos
mkdir -p /home/user/datastore/media/thumbs
mkdir -p /home/user/datastore/logs/app
mkdir -p /home/user/datastore/logs/system
mkdir -p /home/user/datastore/databases/backups

# Create projects files
python3 -c "open('/home/user/datastore/projects/alpha/main.c','w').write('x'*18200)"
python3 -c "open('/home/user/datastore/projects/alpha/README.md','w').write('a'*512)"
python3 -c "open('/home/user/datastore/projects/beta/app.py','w').write('b'*43008)"
python3 -c "open('/home/user/datastore/projects/beta/config.yaml','w').write('c'*1024)"
python3 -c "open('/home/user/datastore/projects/shared/utils.py','w').write('d'*7680)"

# Create media files
python3 -c "open('/home/user/datastore/media/images/photo1.jpg','w').write('e'*92160)"
python3 -c "open('/home/user/datastore/media/images/photo2.jpg','w').write('f'*87040)"
python3 -c "open('/home/user/datastore/media/videos/clip.mp4','w').write('g'*204800)"
python3 -c "open('/home/user/datastore/media/thumbs/thumb1.png','w').write('h'*3072)"

# Create logs files
python3 -c "open('/home/user/datastore/logs/app/app.log','w').write('i'*34816)"
python3 -c "open('/home/user/datastore/logs/app/error.log','w').write('j'*8192)"
python3 -c "open('/home/user/datastore/logs/system/syslog','w').write('k'*15360)"

# Create databases files
python3 -c "open('/home/user/datastore/databases/db1.sqlite','w').write('l'*46080)"
python3 -c "open('/home/user/datastore/databases/db2.sqlite','w').write('m'*20480)"
python3 -c "open('/home/user/datastore/databases/backups/db1_bak.sqlite','w').write('n'*46080)"

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
