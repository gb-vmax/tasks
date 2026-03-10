I'm a web developer cleaning up and preparing a project for deployment. My project lives at `/home/user/webapp`. I need your help running several batch file operations to get it ready. Here's what needs to happen:

**Background:** The project has a messy mix of source files, stale cache files, backup files, and assets scattered across subdirectories. I need to clean it up, process some files, and generate a deployment manifest.

---

### Task 1: Delete stale cache and backup files

Using `find` and `xargs`, delete all files that match either of these patterns anywhere under `/home/user/webapp`:
- Files ending in `.cache`
- Files ending in `.bak`

Do not delete any directories, only files.

---

### Task 2: Compress all `.log` files

Using `find` and `xargs`, run `gzip` on every `.log` file found anywhere under `/home/user/webapp`. This should compress each file in-place (resulting in `.log.gz` files, with the original `.log` files no longer present).

---

### Task 3: Inject a deployment marker into every `.html` file

Using `find` and `xargs`, append exactly the following line to the end of every `.html` file found anywhere under `/home/user/webapp`:

```
<!-- deployed: v2.4.1 -->
```

Every HTML file must have this line appended, even if the file already has content. Use `sed -i` or `bash -c` with `echo >>` as you see fit, but each file must end with that exact line (with a newline after it, i.e., that line is a complete line in the file).

---

### Task 4: Collect a sorted list of all `.js` and `.css` files into a manifest

Using `find` and `xargs` (or `find` alone with appropriate options), produce a file at `/home/user/webapp/deploy_manifest.txt`. This file must contain:

1. A header line: `=== Deploy Manifest ===`
2. One line per `.js` or `.css` file found anywhere under `/home/user/webapp`, showing the file's path relative to `/home/user/webapp` (i.e., strip the `/home/user/webapp/` prefix), sorted alphabetically (standard `sort` order).
3. A footer line: `=== Total: N files ===` where `N` is the count of `.js` and `.css` files listed.

The `deploy_manifest.txt` file itself should NOT be included in any of the operations above (it's not `.html`, `.log`, `.js`, `.css`, `.cache`, or `.bak`, so it naturally won't be, but just be aware).

Example format (with made-up filenames):
```
=== Deploy Manifest ===
assets/css/main.css
assets/css/reset.css
assets/js/app.js
src/components/widget.js
=== Total: 4 files ===
```

---

### Verification notes:

- After all operations: no `.cache` or `.bak` files should exist anywhere under `/home/user/webapp`.
- After all operations: no `.log` files (uncompressed) should exist anywhere under `/home/user/webapp`; only `.log.gz` files.
- Every `.html` file under `/home/user/webapp` must have `<!-- deployed: v2.4.1 -->` as its final line.
- `/home/user/webapp/deploy_manifest.txt` must exist and follow the exact format described, with the correct count.
