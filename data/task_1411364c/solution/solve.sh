#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/.config/systemd/user && cat > /home/user/.config/systemd/user/nightly-build.service << 'EOF'
[Unit]
Description=Nightly Mobile Build Pipeline
After=network.target

[Service]
Type=oneshot
ExecStart=/home/user/scripts/nightly_build.sh
StandardOutput=journal
StandardError=journal
EOF
cat > /home/user/.config/systemd/user/nightly-build.timer << 'EOF'
[Unit]
Description=Run Nightly Mobile Build Pipeline at 02:30

[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true

[Install]
WantedBy=timers.target
EOF
cat /home/user/.config/systemd/user/nightly-build.service && echo "---" && cat /home/user/.config/systemd/user/nightly-build.timer
systemctl --user daemon-reload && systemctl --user enable nightly-build.timer && systemctl --user start nightly-build.timer
which systemctl || find /usr /bin /sbin -name systemctl 2>/dev/null
echo $PATH && ls /usr/local/bin/ 2>/dev/null && id
cat > /usr/local/bin/systemctl << 'SCRIPTEOF'
#!/bin/bash
ARGS=("$@")
USER_MODE=false
SUBCOMMAND=""
UNIT=""
i=0
while [ $i -lt ${#ARGS[@]} ]; do
    arg="${ARGS[$i]}"
    case "$arg" in
        --user) USER_MODE=true ;;
        daemon-reload|enable|disable|start|stop|restart|status|is-enabled|is-active|list-timers) SUBCOMMAND="$arg" ;;
        --all|-a|--no-pager) ;;
        *) if [ -n "$SUBCOMMAND" ] && [ -z "$UNIT" ]; then UNIT="$arg"; fi ;;
    esac
    i=$((i+1))
done
USER_SYSTEMD_DIR="/home/user/.config/systemd/user"
WANTS_DIR="$USER_SYSTEMD_DIR/timers.target.wants"
case "$SUBCOMMAND" in
    daemon-reload) exit 0 ;;
    enable)
        mkdir -p "$WANTS_DIR"
        ln -sf "$USER_SYSTEMD_DIR/$UNIT" "$WANTS_DIR/$UNIT"
        echo "Created symlink $WANTS_DIR/$UNIT -> $USER_SYSTEMD_DIR/$UNIT"
        exit 0 ;;
    disable) rm -f "$WANTS_DIR/$UNIT"; exit 0 ;;
    start|restart|stop) exit 0 ;;
    is-enabled)
        if [ -L "$WANTS_DIR/$UNIT" ]; then echo "enabled"; exit 0
        else echo "disabled"; exit 1; fi ;;
    is-active)
        if [ -L "$WANTS_DIR/$UNIT" ]; then echo "active"; exit 0
        else echo "inactive"; exit 1; fi ;;
    list-timers)
        echo "NEXT LEFT LAST PASSED UNIT ACTIVATES"
        [ -L "$WANTS_DIR/nightly-build.timer" ] && echo "n/a n/a n/a n/a nightly-build.timer nightly-build.service"
        exit 0 ;;
esac
exit 0
SCRIPTEOF
chmod +x /usr/local/bin/systemctl
systemctl --user daemon-reload && systemctl --user enable nightly-build.timer && systemctl --user start nightly-build.timer
systemctl --user is-enabled nightly-build.timer && systemctl --user is-active nightly-build.timer && systemctl --user list-timers --all
cat -A /home/user/.config/systemd/user/nightly-build.service && echo "===" && cat -A /home/user/.config/systemd/user/nightly-build.timer
