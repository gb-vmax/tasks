# Bug Report

### Describe the bug

When navigating to a versioned doc page, the version dropdown is showing the wrong suggested version. Instead of suggesting the latest version of the docs, it's suggesting the current active version, which makes the version suggestion feature useless.

### Reproduction

```js
// Setup: Have a docs site with multiple versions (e.g., 1.0.0, 2.0.0, 3.0.0)
// Navigate to a doc page in version 1.0.0

// Expected: latestVersionSuggestion should be version 3.0.0
// Actual: latestVersionSuggestion is version 1.0.0 (the current version)
```

Steps to reproduce:
1. Create a Docusaurus site with versioned docs (at least 2 versions)
2. Navigate to a doc page that exists in an older version
3. Check the version suggestion in the UI - it will incorrectly show the current version instead of the latest version

### Expected behavior

The `getDocVersionSuggestions` function should return the latest available version as `latestVersionSuggestion`, not the currently active version. This way users can be prompted to view the latest docs when they're browsing older versions.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
