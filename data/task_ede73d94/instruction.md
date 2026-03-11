Hey, I need your help fixing some permission issues on our observability dashboard config files. I'm a dashboard engineer and my team just onboarded a new read-only monitoring user (`observer`) who needs to view dashboard configs, but NOT modify them. Meanwhile, the dashboard config files need to be locked down so that "other" users (world) have zero permissions.

Here's the situation:

The dashboard configuration directory is at `/home/user/dashboards`. It contains three files:

- `grafana_main.json` — the primary dashboard config
- `alerts_config.json` — alert thresholds and routing rules
- `datasources.cfg` — database connection settings (this one is sensitive)

**What I need you to do:**

1. Change the permissions on all three files so that:
   - The **owner** (`user`) has **read and write** permissions.
   - The **group** has **read-only** permissions.
   - **Others** have **no permissions at all**.

2. Change the **group ownership** of all three files to `observer`.

After your changes, running `ls -l /home/user/dashboards/` should show each file with permissions `-rw-r-----` and group `observer`.

The exact output of `ls -l /home/user/dashboards/` should look like this (the date and inode details will vary, but permissions, owner, and group must match exactly):

```
total 12
-rw-r----- 1 user observer  ... alerts_config.json
-rw-r----- 1 user observer  ... datasources.cfg
-rw-r----- 1 user observer  ... grafana_main.json
```

(Files are listed alphabetically as `ls` normally does. The `...` represents the file size and timestamp which will vary.)

Please make these permission changes now.
