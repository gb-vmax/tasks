# Bug Report

### Describe the bug

I'm experiencing an issue where files are being written even when their content hasn't changed. It seems like the caching mechanism that's supposed to prevent unnecessary file writes isn't working correctly.

### Reproduction

```js
const { generate } = require('@docusaurus/utils');

// Generate a file with some content
await generate(generatedFilesDir, 'example.txt', 'Hello World');

// Try to generate the same file again with identical content
await generate(generatedFilesDir, 'example.txt', 'Hello World');

// Expected: File should not be rewritten (cached)
// Actual: File is being written again even though content is the same
```

### Expected behavior

When generating a file with the same content as what already exists, the `generate` function should skip writing to disk and use the cached hash instead. This would prevent unnecessary file system operations and improve build performance.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing performance issues during builds as files are being unnecessarily rewritten on every generation, even when nothing has changed.

---
Repository: /testbed
