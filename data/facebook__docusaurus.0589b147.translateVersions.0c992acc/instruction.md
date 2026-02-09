# Bug Report

### Describe the bug

After updating to the latest version, I'm seeing duplicate version entries in my documentation site. It looks like the versioned docs are being processed incorrectly - the last version appears twice and the first version is missing from the list.

### Reproduction

Setup a docs site with multiple versions:
```
versions.json:
["2.0.0", "1.5.0", "1.0.0"]
```

When the site builds, the resulting version list shows:
- 1.5.0
- 1.0.0  
- 1.0.0 (duplicate)

The first version (2.0.0) is completely missing from the output.

### Expected behavior

All versions should be present exactly once in the correct order:
- 2.0.0
- 1.5.0
- 1.0.0

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking our multi-version documentation setup. Any help would be appreciated!

---
Repository: /testbed
