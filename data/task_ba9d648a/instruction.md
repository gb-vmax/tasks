Hey, I'm a network engineer and I've been reorganizing our router configuration files. We have a directory structure for our configs, but I need your help setting up some symbolic links so that our monitoring scripts (which look for configs in a specific "active" directory) can find the right files without us duplicating everything.

Here's the situation:

Our router configuration files live in `/home/user/network/configs/`. There are several `.conf` files there for different routers. Our monitoring system always looks in `/home/user/network/active/` for the currently active configurations. Right now, that directory exists but is empty.

I need you to do the following:

1. Create a symbolic link inside `/home/user/network/active/` called `core-router.conf` that points to the **absolute path** `/home/user/network/configs/core-router.conf`.

2. Create a symbolic link inside `/home/user/network/active/` called `edge-router.conf` that points to the **absolute path** `/home/user/network/configs/edge-router.conf`.

3. Our legacy monitoring script is hardcoded to look for a file called `primary.conf` in `/home/user/network/active/`. Create another symbolic link at `/home/user/network/active/primary.conf` that points to the **absolute path** `/home/user/network/configs/core-router.conf` (same underlying file as `core-router.conf`, just a different link name).

4. Finally, write a plain text file at `/home/user/network/active/links.txt` that documents what symlinks exist in that directory. The file should contain exactly these 3 lines (and no others), in this exact order:

```
core-router.conf -> /home/user/network/configs/core-router.conf
edge-router.conf -> /home/user/network/configs/edge-router.conf
primary.conf -> /home/user/network/configs/core-router.conf
```

Each line should be in the format `<link_name> -> <target_path>` exactly as shown above (single space, arrow `->`, single space). The lines must be in alphabetical order by link name.

To verify everything looks right, make sure that running `readlink /home/user/network/active/core-router.conf` returns `/home/user/network/configs/core-router.conf`, and similarly for the other two links. The symlinks must point to absolute paths, not relative ones.
