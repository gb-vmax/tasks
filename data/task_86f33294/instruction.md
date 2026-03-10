Hey, I need help with a deployment task. We use a symlink-based deployment strategy where `/home/user/deployments/current` always points to the active release directory. Right now it points to an old version and I need to roll it forward to a new release.

Here's the current state of the filesystem:

- `/home/user/deployments/releases/v2.3.1/` — the currently active release (this is what `current` points to right now)
- `/home/user/deployments/releases/v2.4.0/` — the new release that was just staged and is ready to go live

Each release directory contains an `app.conf` file and a `version.txt` file.

I need you to do the following:

1. Update the symlink `/home/user/deployments/current` so that it points to `/home/user/deployments/releases/v2.4.0` instead of the old release. The symlink must use an **absolute path** as its target (not a relative path).

2. Create a new symlink at `/home/user/deployments/previous` that points to `/home/user/deployments/releases/v2.3.1` (also using an absolute path), so we have a quick reference to the last release in case we need to roll back.

3. Write a small deployment record to `/home/user/deployments/deploy_log.txt`. The file should contain exactly these two lines (no extra blank lines, no trailing spaces):

```
current -> /home/user/deployments/releases/v2.4.0
previous -> /home/user/deployments/releases/v2.3.1
```

This file should reflect the actual resolved symlink targets — you can generate it by reading the symlinks themselves (e.g., using `readlink` or similar) rather than hardcoding the strings, so it stays accurate.

Can you get this done? After you're finished, I'll verify by checking:
- That `readlink /home/user/deployments/current` outputs `/home/user/deployments/releases/v2.4.0`
- That `readlink /home/user/deployments/previous` outputs `/home/user/deployments/releases/v2.3.1`
- That the contents of `/home/user/deployments/deploy_log.txt` match exactly what's shown above
