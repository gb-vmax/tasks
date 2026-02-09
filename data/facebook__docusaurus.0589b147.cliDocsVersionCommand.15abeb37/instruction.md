# Bug Report

### Describe the bug

When creating a new docs version using the CLI, the version is being added to the wrong position in the versions array. Instead of being added at the beginning (as the latest/current version), it's being appended to the end of the versions list.

### Reproduction

1. Initialize a Docusaurus site with versioned docs
2. Create an initial version: `docusaurus docs:version 1.0.0`
3. Create a second version: `docusaurus docs:version 2.0.0`
4. Check the `versions.json` file

**Actual result:**
```json
[
  "1.0.0",
  "2.0.0"
]
```

**Expected result:**
```json
[
  "2.0.0",
  "1.0.0"
]
```

The newest version should appear first in the array since Docusaurus treats the first element as the current/latest version.

### Expected behavior

New versions should be prepended to the versions array (added at index 0) so that the most recent version is always first. This affects which version is displayed by default and how version dropdowns are ordered.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
