# Bug Report

### Describe the bug

The `logger.success()` function is not handling template string interpolation correctly. When calling it with template literals and values, the interpolation doesn't work as expected - it seems to ignore the provided values.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This doesn't interpolate the value correctly
logger.success`Found ${5} items`;

// Expected output: [SUCCESS] Found 5 items
// Actual output: [SUCCESS] Found ${5} items (or similar incorrect output)
```

Also happens with multiple values:

```js
logger.success`Processing ${10} files in ${2} directories`;
```

### Expected behavior

When using template literal syntax with `logger.success`, the values should be properly interpolated into the message string, similar to how regular template literals work.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
