I'm a data engineer and I have an ETL pipeline script that needs to run automatically on a schedule. The script already exists at `/home/user/etl/run_pipeline.sh` and is executable.

I want you to set up a **user-level systemd timer** (not a crontab entry) that runs this script every day at 02:30 AM. Please create the two required unit files for a systemd user timer:

1. A service unit file at `/home/user/.config/systemd/user/etl-pipeline.service`
2. A timer unit file at `/home/user/.config/systemd/user/etl-pipeline.timer`

The service unit file must have the following exact structure and values:
- Section `[Unit]` with `Description` set to `ETL Pipeline Job`
- Section `[Service]` with `Type` set to `oneshot` and `ExecStart` set to `/home/user/etl/run_pipeline.sh`

The timer unit file must have the following exact structure and values:
- Section `[Unit]` with `Description` set to `Run ETL Pipeline daily at 02:30`
- Section `[Timer]` with `OnCalendar` set to `*-*-* 02:30:00` and `Persistent` set to `true`
- Section `[Install]` with `WantedBy` set to `timers.target`

After creating both files, enable the timer using `systemctl --user enable etl-pipeline.timer` so that it is activated on login (this creates the necessary symlink in `/home/user/.config/systemd/user/timers.target.wants/`).

The directory `/home/user/.config/systemd/user/` may not exist yet — please create it if needed.

Can you set all of this up for me?
