Hey, I need your help bumping the version and updating the changelog for our API integration library. The library lives at `/home/user/api-client`. Here's the situation:

We just finished adding a new OAuth2 token refresh feature and fixed a bug where GET requests with empty query params were failing. I need to cut a new **minor version release** (following semantic versioning) before I run my integration tests against the staging environment.

Here's what I need you to do:

**Step 1: Read the current version**

The current version is stored in `/home/user/api-client/VERSION`. It contains a single line with the version number in `MAJOR.MINOR.PATCH` format. You need to bump the **MINOR** version by 1 and reset the **PATCH** version to 0. The MAJOR version stays the same. Overwrite `/home/user/api-client/VERSION` with the new version (a single line, no leading/trailing whitespace, no `v` prefix).

**Step 2: Update the changelog**

The changelog lives at `/home/user/api-client/CHANGELOG.md`. You need to **prepend** a new entry for the new version at the top of the file, above all existing content. The new entry must follow this exact format (including blank lines):

```
## [<NEW_VERSION>] - 2024-06-15

### Added
- OAuth2 token refresh support

### Fixed
- GET requests no longer fail when query params are empty

```

There must be exactly one blank line between the new entry and whatever was already at the top of the file. Do not modify any existing content in the file — only prepend.

**Step 3: Verify the result**

After making those changes, print the contents of `/home/user/api-client/VERSION` to the terminal (just the version string), and then print the first 12 lines of `/home/user/api-client/CHANGELOG.md` to the terminal.

The final `/home/user/api-client/VERSION` file should contain only the new version number on a single line. The final `/home/user/api-client/CHANGELOG.md` should have your new entry at the very top, followed by a blank line, then the original content unchanged.

Can you handle that for me?
