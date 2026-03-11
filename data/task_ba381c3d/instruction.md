Hey, I need help organizing my project directory. I've got a messy `/home/user/project` folder with a bunch of source and build artifact files scattered around in subdirectories. I want to do a few cleanup steps to get things tidy.

Here's what I need done:

**Step 1: Move all `.log` files to a centralized log archive directory.**

Find every `.log` file anywhere under `/home/user/project` and move them all into `/home/user/project/logs_archive`. The destination directory already exists. Use `find` piped into `xargs` to do this in a single batch operation.

**Step 2: Delete all `.tmp` files under `/home/user/project`.**

Find every file with the `.tmp` extension anywhere under `/home/user/project` (excluding `logs_archive`) and delete them all using `find` and `xargs`. There may be several of them in different subdirectories.

**Step 3: Generate a manifest of all remaining `.py` files.**

After the cleanup above, find all `.py` files anywhere under `/home/user/project`, and write their paths to `/home/user/project/py_manifest.txt`. Each line should be an absolute path. The lines must be sorted alphabetically. The file should contain one path per line with no trailing blank lines.

The manifest file should be created using `find` and `sort`, writing the result to `/home/user/project/py_manifest.txt`.

Please make sure the final state is:
- All `.log` files are in `/home/user/project/logs_archive/` (and nowhere else under the project tree)
- No `.tmp` files exist anywhere under `/home/user/project`
- `/home/user/project/py_manifest.txt` exists and lists every `.py` file under the project tree, one absolute path per line, sorted alphabetically
