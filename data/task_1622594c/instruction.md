I'm an operations engineer and I need your help triaging a production incident. We've identified that the application server at `/home/user/incident/logs` contains several log files, but I only need to archive the ones that end in `.error` for a post-mortem review. I need you to bundle all the `.error` log files from that directory into a single compressed tarball and then verify what's inside.

Specifically, please do the following:

1. Create a gzip-compressed tar archive called `incident_errors.tar.gz` inside the `/home/user/incident/` directory. The archive must contain **only** the files ending in `.error` from `/home/user/incident/logs/`. The files should be archived using relative paths (i.e., paths inside the archive should look like `logs/app.error`, not `/home/user/incident/logs/app.error`).

2. List the contents of the resulting archive and save that listing to `/home/user/incident/archive_manifest.txt`. The listing must be in verbose format (using `tar -tvf`) so each line shows permissions, owner, size, date, and filename. The file should contain exactly one line per archived file (no header lines, no trailing blank lines, just the file entries). Redirect the output of the `tar -tvf` command directly into `archive_manifest.txt`.

The directory `/home/user/incident/logs/` contains these files — make sure all `.error` files and none of the non-`.error` files end up in the archive:
- `app.error`
- `db.error`
- `nginx.error`
- `app.log`
- `db.log`
- `system.info`

After you're done, I should be able to see that `incident_errors.tar.gz` exists at `/home/user/incident/incident_errors.tar.gz` and that `archive_manifest.txt` contains exactly 3 lines corresponding to the three `.error` files.
