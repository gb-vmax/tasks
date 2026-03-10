Hey, I need help setting up a scheduled build pipeline task on my Linux workstation. I'm a mobile build engineer and I have a nightly build script that needs to run automatically. I want to use a **systemd user timer** (not cron) so it integrates with my user session properly.

Here's what I need:

There's already a build script at `/home/user/scripts/nightly_build.sh`. I need you to create a systemd user service and timer that runs this script automatically every night.

**Step 1: Create the systemd user service unit**

Create the file `/home/user/.config/systemd/user/nightly-build.service` with the following content exactly:

```
[Unit]
Description=Nightly Mobile Build Pipeline
After=network.target

[Service]
Type=oneshot
ExecStart=/home/user/scripts/nightly_build.sh
StandardOutput=journal
StandardError=journal
```

Note: there should be no `[Install]` section — the timer will activate it.

**Step 2: Create the systemd user timer unit**

Create the file `/home/user/.config/systemd/user/nightly-build.timer` with the following content exactly:

```
[Unit]
Description=Run Nightly Mobile Build Pipeline at 02:30

[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true

[Install]
WantedBy=timers.target
```

The `Persistent=true` directive ensures the build runs at 02:30 even if the machine was off at that time.

**Step 3: Enable and start the timer**

Enable the timer so it persists across reboots and start it so it's active immediately, using systemd user mode (`--user` flag). Do NOT enable or start the `.service` unit directly — only the `.timer` unit should be enabled and started.

**Step 4: Verify it worked**

After enabling and starting, confirm the timer is loaded and active by listing user timers. The output of `systemctl --user list-timers --all` should show `nightly-build.timer` in the list with the `UNIT` column displaying `nightly-build.timer`.

The automated test will check:
1. The exact contents of `/home/user/.config/systemd/user/nightly-build.service` — must match the content above byte-for-byte (including a trailing newline).
2. The exact contents of `/home/user/.config/systemd/user/nightly-build.timer` — must match the content above byte-for-byte (including a trailing newline).
3. That `systemctl --user is-enabled nightly-build.timer` outputs `enabled`.
4. That `systemctl --user is-active nightly-build.timer` outputs `active`.
