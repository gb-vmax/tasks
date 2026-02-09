# Bug Report

### Describe the bug

I'm experiencing an issue with path handling in the docs plugin. When processing file paths with number prefixes, the path segments are being joined with hyphens (`-`) instead of forward slashes (`/`), which completely breaks the expected path structure.

### Reproduction

```js
// Input path with number prefixes
const inputPath = '01-intro/02-getting-started/03-installation'

// After stripPathNumberPrefixes is called
// Expected: 'intro/getting-started/installation'
// Actual: 'intro-getting-started-installation'
```

This is causing problems when the plugin tries to resolve document paths - instead of getting proper nested paths, everything is flattened into a single level with hyphens.

### Expected behavior

The function should strip number prefixes from each path segment but maintain the directory structure by joining segments with forward slashes. The output should be a valid file path, not a hyphenated string.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
