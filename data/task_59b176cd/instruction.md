I'm maintaining a Kubernetes operator project and need to cut a new release. The project lives at `/home/user/operator`. It has a `VERSION` file containing the current version, and a `CHANGELOG.md` with the history of past releases.

I've already staged the commits for this release cycle, but I need you to:

1. **Determine the correct semantic version bump** by inspecting the file `/home/user/operator/pending_commits.txt`, which lists the commit messages for this release cycle (one per line). Use these rules:
   - If any commit message starts with `breaking:`, bump the **major** version (and reset minor and patch to 0).
   - Otherwise, if any commit message starts with `feat:`, bump the **minor** version (and reset patch to 0).
   - Otherwise, bump the **patch** version only.

2. **Update `/home/user/operator/VERSION`** so it contains exactly the new version string and nothing else (no newline, no extra whitespace — just the version like `1.4.0`).

3. **Prepend a new entry to `/home/user/operator/CHANGELOG.md`** for the new version. The entry must appear at the very top of the file, before any existing content. The format must be exactly:

```
## [<new_version>] - 2024-11-15

### Changed
<list of commit messages, each prefixed with "- ", in the same order they appear in pending_commits.txt>

---
```

Then the existing content of `CHANGELOG.md` follows immediately after the `---` line (with a single newline separating the `---` from the existing content).

For example, if the new version is `1.4.0` and there are two commits, the top of the file should look like:

```
## [1.4.0] - 2024-11-15

### Changed
- feat: add leader election support
- fix: handle nil pointer in reconcile loop

---
## [1.3.0] - 2024-10-02
...
```

The date must be exactly `2024-11-15`. The `---` separator line must be on its own line with nothing after it except a newline before the old content begins.

Please make these two changes to the files. Do not create any other files.
