Hi, I'm a site administrator and I need help updating the version number and changelog for our user account management tool. I have two files in `/home/user/accounttool/`:

1. `/home/user/accounttool/VERSION` — contains the current semantic version as a single line (e.g., `2.4.1`)
2. `/home/user/accounttool/COMMITS` — contains a list of recent commit messages, one per line, using conventional commit format

I need you to:

**Step 1: Determine the version bump type.**

Read the `COMMITS` file and apply these rules to figure out what kind of semver bump is needed:
- If ANY line starts with `feat!:` or `fix!:` or contains `BREAKING CHANGE` → bump the **major** version
- Otherwise, if ANY line starts with `feat:` → bump the **minor** version
- Otherwise (only `fix:`, `chore:`, `docs:`, etc.) → bump the **patch** version

Apply only the highest-priority rule that matches.

**Step 2: Compute the new version.**

Read the current version from `/home/user/accounttool/VERSION`, apply the bump:
- **major** bump: increment first number, reset second and third to 0
- **minor** bump: increment second number, reset third to 0
- **patch** bump: increment third number only

Write the new version (just the version string, no trailing newline) back to `/home/user/accounttool/VERSION`.

**Step 3: Update the changelog.**

Append a new entry to `/home/user/accounttool/CHANGELOG.md`. If the file does not exist, create it. The entry must be appended at the **bottom** of the file and follow this exact format (note the blank line before the version header if the file already has content):

```
## v<new_version>

<categorized commit lines>
```

The categorized commit lines must:
- Group commits under bold headers: `**Breaking Changes**`, `**Features**`, `**Bug Fixes**`, `**Other**`
- Only include a header if there is at least one commit in that category
- Under each header, list each matching commit as `- <full original commit message>` (include the prefix like `feat:`, `fix!:`, etc.)
- Order of headers: Breaking Changes first, then Features, then Bug Fixes, then Other
- Categories: lines starting with `feat!:` or `fix!:` or containing `BREAKING CHANGE` → Breaking Changes; `feat:` → Features; `fix:` → Bug Fixes; everything else → Other
- A single commit that qualifies as Breaking Changes should appear ONLY under Breaking Changes, not also under Features or Bug Fixes

For example, if the new version is `2.5.0` and there are commits `feat: add avatar upload` and `fix: correct session timeout`, the appended block would look like:

```
## v2.5.0

**Features**
- feat: add avatar upload

**Bug Fixes**
- fix: correct session timeout
```

The file `/home/user/accounttool/CHANGELOG.md` already has some existing content before you append. Do not modify the existing content — only append to the end.
