# Bug Report

### Describe the bug

After a recent update, Git repository URIs are being automatically normalized/modified when loading existing repositories. This is causing issues with repositories that have specific URI formats, particularly SSH URLs and URLs with trailing slashes or `.git` extensions.

### Reproduction

1. Create a Git repository with an SSH URI format like `git@github.com:user/repo.git`
2. Save and reload the repository
3. The URI gets automatically converted to HTTPS format: `https://github.com/user/repo`

Similarly, if you have a repository with a URI like:
- `https://example.com/repo/` (with trailing slash)
- `https://example.com/repo.git` (with .git extension)

These get normalized to `https://example.com/repo` without the trailing slash or extension.

### Expected behavior

The repository URI should remain unchanged from what was originally configured. Users should be able to use SSH URIs, trailing slashes, and `.git` extensions if they want to. The automatic normalization is breaking existing repository configurations.

### Additional context

This appears to have been introduced in a migration function that's now being applied to all repositories on load. The normalization is happening even for repositories that don't need migration.

---
Repository: /testbed
