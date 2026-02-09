# Bug Report

### Describe the bug

When using the `generate()` function from `@docusaurus/utils`, files are not being written to disk even when their content has changed. This causes the build output to become stale and not reflect the latest content updates.

### Reproduction

```js
import {generate} from '@docusaurus/utils';

// First write
await generate(__dirname, 'test.txt', 'original content');

// Update with new content
await generate(__dirname, 'test.txt', 'updated content');

// File on disk still contains "original content" instead of "updated content"
```

### Expected behavior

The file should be updated on disk when the content changes. The function should write the new content when it detects a difference between the current hash and the last hash.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is blocking our build process as changes to generated files are not being persisted correctly.

---
Repository: /testbed
