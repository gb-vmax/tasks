# Bug Report

### Describe the bug

When using `logger.report()` with `reportingSeverity: 'throw'`, the logger is now calling `warn()` instead of actually throwing an error. This means error conditions that should halt execution are being silently logged as warnings instead.

### Reproduction

```js
const logger = require('@docusaurus/logger');

// This should throw an error but only logs a warning
logger.report('throw')('This is a critical error');

console.log('This line should not be reached if throw worked correctly');
```

### Expected behavior

When `reportingSeverity` is set to `'throw'`, the logger should throw an error and stop execution. Currently it just logs a warning and continues.

### Additional context

This is causing issues in our build pipeline where we expect the process to fail on certain validation errors, but instead the build completes successfully even when critical errors occur.

---
Repository: /testbed
