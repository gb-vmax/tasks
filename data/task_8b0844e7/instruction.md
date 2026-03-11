I'm setting up automated provisioning for a web service and need help managing versioned configuration files with symbolic links. The infrastructure uses a pattern where the "active" config is always a symlink pointing to a specific versioned file, so we can roll back instantly by updating the symlink.

Here's the situation: I have versioned nginx config files sitting in `/home/user/configs/versions/`. Right now the directory contains these two files:
- `nginx.conf.v1` — the old version (already deployed previously)
- `nginx.conf.v2` — the new version I want to activate

There's also an "active" directory at `/home/user/configs/active/` where the live symlinks live. Currently it contains a symlink called `nginx.conf` that points to `/home/user/configs/versions/nginx.conf.v1` (the old version).

I need you to update the active symlink so that `/home/user/configs/active/nginx.conf` points to `/home/user/configs/versions/nginx.conf.v2` instead of v1. The symlink must be an absolute path symlink (not relative). The old symlink should be replaced — there should only be one symlink named `nginx.conf` in that directory when you're done.

After updating the symlink, please write a one-line plain text record of the change to `/home/user/configs/provision.log`. The line must follow this exact format (including spacing and punctuation):

```
nginx.conf -> /home/user/configs/versions/nginx.conf.v2
```

That is: the symlink name, a space, `->`, a space, and then the absolute target path. There should be no trailing newline issues — the file should contain exactly that one line followed by a newline character.
