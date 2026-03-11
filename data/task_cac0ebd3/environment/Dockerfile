FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create artifact directories
mkdir -p /home/user/artifacts/v1.0 /home/user/artifacts/v1.1 /home/user/artifacts/v1.2

# Create binary files with specific content and sizes
python3 -c "open('/home/user/artifacts/v1.0/app.bin','wb').write(b'A'*1024)"
python3 -c "open('/home/user/artifacts/v1.0/libcore.so','wb').write(b'B'*2048)"
echo "Release v1.0" > /home/user/artifacts/v1.0/README.txt
python3 -c "open('/home/user/artifacts/v1.1/app.bin','wb').write(b'C'*1536)"
printf '#!/bin/bash\necho install\n' > /home/user/artifacts/v1.1/installer.sh
python3 -c "open('/home/user/artifacts/v1.2/app.bin','wb').write(b'D'*2048)"
python3 -c "open('/home/user/artifacts/v1.2/librender.so','wb').write(b'E'*512)"
echo "Bug fixes" > /home/user/artifacts/v1.2/CHANGES.txt

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
