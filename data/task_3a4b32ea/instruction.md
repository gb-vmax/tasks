Hey, I've got a really messy project directory at `/home/user/project` that I need to reorganize. It's full of files dumped in a flat structure and I need to sort everything into a proper layout, set the right permissions, create some convenience symlinks, and generate a manifest file. Can you help me get this all sorted out?

Here's what the directory currently contains (all files directly under `/home/user/project/`):

- Source files: `main.c`, `utils.c`, `parser.c`, `utils.h`, `parser.h`, `config.h`
- Python scripts: `build.py`, `deploy.py`, `test_runner.py`
- Documentation: `README.md`, `CHANGELOG.md`, `API.md`
- Configuration files: `app.conf`, `db.conf`, `logging.conf`
- Log files: `app.log`, `error.log`, `debug.log`
- Data files: `seed.sql`, `schema.sql`, `fixtures.json`

I need you to reorganize this into the following structure and then do several additional tasks:

---

**Step 1: Create the directory layout and move files**

Create these subdirectories and move the files into them:

- `/home/user/project/src/` — move all `.c` and `.h` files here
- `/home/user/project/scripts/` — move all `.py` files here
- `/home/user/project/docs/` — move all `.md` files here
- `/home/user/project/config/` — move all `.conf` files here
- `/home/user/project/logs/` — move all `.log` files here
- `/home/user/project/data/` — move all `.sql` and `.json` files here

---

**Step 2: Set file permissions**

- All files in `src/` should have permissions `644`
- All files in `scripts/` should have permissions `755` (they are executable scripts)
- All files in `docs/` should have permissions `644`
- All files in `config/` should have permissions `600` (sensitive config files)
- All files in `logs/` should have permissions `640`
- All files in `data/` should have permissions `644`

---

**Step 3: Create symlinks**

Create the following symlinks directly under `/home/user/project/`:

- `project.conf` → symlink pointing to `config/app.conf`
- `run.py` → symlink pointing to `scripts/build.py`
- `latest.log` → symlink pointing to `logs/app.log`

The symlinks should use relative targets (e.g., `config/app.conf`, not `/home/user/project/config/app.conf`).

---

**Step 4: Generate a manifest file**

Create a file at `/home/user/project/manifest.txt` with a listing of all non-symlink files (regular files only) under `/home/user/project/`, sorted alphabetically by their path. The manifest must use this exact format — one line per file, with the relative path (relative to `/home/user/project/`), a single space, and then the octal permission bits (just the 3-digit permission number, as reported by `stat`):

```
config/app.conf 600
config/db.conf 600
config/logging.conf 600
data/fixtures.json 644
...
```

The manifest should NOT include `manifest.txt` itself, and should NOT include any symlinks or directories — only regular files. The paths should use forward slashes and not begin with `./`. Sort the entries strictly alphabetically by the path column.

---

The final state I want is:
- All original files moved into their correct subdirectories (no loose files left in `/home/user/project/` except the three symlinks and `manifest.txt`)
- Correct permissions on every file
- Three working symlinks at the project root
- A `manifest.txt` with exactly the format described above listing all 16 regular files in their new locations, sorted alphabetically

Please get this done!
