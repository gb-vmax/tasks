FROM endless-base:latest

RUN <<'ENDPOST'
set -e

    apt-get update
    apt-get install -y python3-pip
    pip3 install pytest

    # Create user and home directory if not exist
    if ! id -u user >/dev/null 2>&1; then
        useradd -m user
    fi

    # Ensure /home/user exists and correct permissions
    mkdir -p /home/user
    chown user:user /home/user

    # Create provisioning/configs directory and config files
    install -d -m 0755 /home/user/provisioning/configs
    echo "WEB.CONF"   > /home/user/provisioning/configs/web.conf
    echo "DB.CONF"    > /home/user/provisioning/configs/db.conf
    echo "CACHE.CONF" > /home/user/provisioning/configs/cache.conf
    chown -R user:user /home/user/provisioning

    # Create provisioning/active directory
    install -d -m 0755 /home/user/provisioning/active
    chown user:user /home/user/provisioning/active

    # Create relative symlinks in provisioning/active
    cd /home/user/provisioning/active
    ln -s ../configs/web.conf web_active.conf
    ln -s ../configs/db.conf db_active.conf
    ln -s ../configs/cache.conf cache_active.conf
    chown -h user:user web_active.conf db_active.conf cache_active.conf

    # Create report file with exact required lines
    cat > /home/user/provisioning/symlink_report.txt <<EOF
web_active.conf,../configs/web.conf,WEB.CONF
db_active.conf,../configs/db.conf,DB.CONF
cache_active.conf,../configs/cache.conf,CACHE.CONF
EOF
    chown user:user /home/user/provisioning/symlink_report.txt
ENDPOST

WORKDIR /home/user
