# Bug Report

### Describe the bug

I'm experiencing an issue with path handling in the docs plugin where paths with number prefixes are being stripped incorrectly. After stripping the number prefixes from path segments, the path separators (`/`) are not being preserved correctly, resulting in malformed paths.

### Reproduction

```js
// Example path with number prefixes
const path = '01-intro/02-getting-started/03-installation'

// After stripping number prefixes, expecting:
// 'intro/getting-started/installation'

// But getting something like:
// 'introgetting-startedinstallation' (missing slashes)
```

### Expected behavior

When stripping number prefixes from a path like `01-intro/02-getting-started`, the result should maintain the path structure with forward slashes: `intro/getting-started`

The path separators should be preserved after removing the numeric prefixes from each segment.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
