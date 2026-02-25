As an observability engineer, you are tuning dashboard configurations stored as JSON files for different environments. You have the following files and directories:

- Configurations are stored in `/home/user/dashboards/` with these files:
  - `prod_dashboard.json`
  - `staging_dashboard.json`
- There is a symbolic link `/home/user/active_dashboard.json` that should point to the dashboard configuration currently in use.
- There are environment directories `/home/user/envs/prod/` and `/home/user/envs/staging/`, each should contain a symbolic link called `dashboard.json` that points to the appropriate configuration file in `/home/user/dashboards/`.

Your task:

1. Update `/home/user/active_dashboard.json` to point to `prod_dashboard.json` in `/home/user/dashboards/`. If a link already exists, replace it.
2. Create or update (if already present) the symbolic link `/home/user/envs/prod/dashboard.json` so it points to `/home/user/dashboards/prod_dashboard.json`.
3. Create or update (if already present) the symbolic link `/home/user/envs/staging/dashboard.json` so it points to `/home/user/dashboards/staging_dashboard.json`.
4. Generate a verification log of your changes at `/home/user/dashboard_symlink_check.log`. The log must specify the absolute path of each symbolic link with its current target, in the following exact format (one link per line, tab-separated, with absolute paths):

```
/home/user/active_dashboard.json	/home/user/dashboards/prod_dashboard.json
/home/user/envs/prod/dashboard.json	/home/user/dashboards/prod_dashboard.json
/home/user/envs/staging/dashboard.json	/home/user/dashboards/staging_dashboard.json
```

Make sure to check and update the symlinks as described, and ensure your log matches the specified output format exactly, with tabs between columns and one line per symlink.
