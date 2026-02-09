# Bug Report

### Describe the bug

When processing markdown files that belong to multiple doc versions (e.g., files in overlapping content paths), the linkify function throws an error instead of handling the file correctly. The error message states that the file "does not belong to any docs version" even though it actually belongs to multiple versions.

### Reproduction

```js
// Setup with overlapping version content paths
const options = {
  versionsMetadata: [
    { contentPath: '/docs' },
    { contentPath: '/docs/v2' }
  ]
}

// File path that matches multiple versions
const filePath = '/docs/v2/example.md'

// This will throw an error about the file not belonging to any version
// even though it matches both versions
```

### Expected behavior

The function should handle files that exist in overlapping content paths without throwing an error. It should either:
- Select the first matching version
- Select the most specific matching version
- Have some defined behavior for this scenario

Currently it just crashes with a misleading error message.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
