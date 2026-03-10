You're a security auditor who just validated that a critical patch was applied to the application at `/home/user/app`. As part of the release process, you need to record the security fix by bumping the patch version and logging it in the changelog.

The repository has two files:

- `/home/user/app/VERSION` — contains a single line with the current semantic version string (e.g., `2.4.7`)
- `/home/user/app/CHANGELOG.md` — an existing changelog file with prior entries

**Task 1: Bump the patch version**

Read the current version from `/home/user/app/VERSION`, increment the patch component by 1 (e.g., `2.4.7` → `2.4.8`), and overwrite `/home/user/app/VERSION` with the new version. The file must contain exactly one line: the new version string with no trailing spaces, no `v` prefix, and a single newline at the end.

**Task 2: Append a changelog entry**

Append the following block to the **end** of `/home/user/app/CHANGELOG.md`, separated from the existing content by a single blank line:

```
## [<new_version>] - 2024-11-15

### Security
- Patched critical input validation vulnerability in authentication module
```

Replace `<new_version>` with the new version string you wrote to `VERSION` (e.g., `2.4.8`). The appended block must match this format exactly — same spacing, same heading levels, same bullet text.

After you are done, `/home/user/app/VERSION` should contain just `2.4.8` (with a newline), and `/home/user/app/CHANGELOG.md` should end with the new entry block as shown above.
