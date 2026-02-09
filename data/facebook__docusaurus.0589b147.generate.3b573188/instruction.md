# Bug Report

### Describe the bug

When using the file generation utilities, files are being written even when their content hasn't changed. This is causing unnecessary file writes and potentially triggering unwanted rebuilds.

### Reproduction

```js
const { generate } = require('@docusaurus/utils');

// First write
await generate(__dirname, 'test.txt', 'hello world', false);

// Second write with same content - should skip writing
await generate(__dirname, 'test.txt', 'hello world', false);

// The file gets written both times even though content is identical
```

### Expected behavior

When the content hash matches the existing file's hash, the file write should be skipped to avoid unnecessary I/O operations and file modification timestamp updates.

### Additional context

This seems to be affecting build performance as files are being rewritten even when they haven't changed, which can trigger watchers and rebuilds unnecessarily.

---
Repository: /testbed
