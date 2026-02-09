# Bug Report

### Describe the bug

After updating to the latest version, Git repository URIs are being modified unexpectedly. When I have a repository URI that already ends with `.git`, the system is appending an additional `.git` suffix, resulting in URIs like `https://github.com/user/repo.git.git`.

### Reproduction

1. Set up a Git repository with a URI that already ends with `.git`
2. The URI gets normalized/migrated
3. The resulting URI has `.git.git` at the end instead of just `.git`

For example:
- Input: `https://github.com/myuser/myrepo.git`
- Expected output: `https://github.com/myuser/myrepo.git`
- Actual output: `https://github.com/myuser/myrepo.git.git`

### Expected behavior

The URI normalization should recognize when a URI already ends with `.git` and not append it again. URIs that already have the correct format should remain unchanged.

### Additional context

This seems to affect both GitHub and GitLab repository URIs. The issue appears when the repository configuration is loaded or migrated.

---
Repository: /testbed
