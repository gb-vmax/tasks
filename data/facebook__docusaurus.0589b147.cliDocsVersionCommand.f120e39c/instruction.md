# Bug Report

### Describe the bug

When creating a new docs version using the CLI command, the version is being added to the end of the versions list instead of at the beginning. This breaks the expected behavior where the newest version should appear first in the versions.json file.

### Reproduction

1. Create a Docusaurus site with versioned docs
2. Run the docs version command to create a new version (e.g., `2.0.0`)
3. Check the `versions.json` file

**Current behavior:**
```json
["1.0.0", "1.1.0", "2.0.0"]
```

**Expected behavior:**
```json
["2.0.0", "1.1.0", "1.0.0"]
```

The newest version should be prepended to the array, not appended. This affects version ordering throughout the documentation site since Docusaurus expects versions to be listed from newest to oldest.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
