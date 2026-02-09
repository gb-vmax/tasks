# Bug Report

### Describe the bug

When using the logger's `report()` function with `reportingSeverity` set to `'ignore'`, passing any arguments causes an infinite recursion. The function keeps calling itself until the stack overflows.

### Reproduction

```js
const logger = require('@docusaurus/logger');

// This causes infinite recursion and crashes
logger.report('ignore')('Some message to ignore');
```

The issue occurs when you try to log a message with the ignore severity level. Instead of silently ignoring the message, it enters an infinite loop.

### Expected behavior

The logger should silently ignore the message without any errors or recursion. It should work the same way as before - just do nothing when ignore is specified.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
