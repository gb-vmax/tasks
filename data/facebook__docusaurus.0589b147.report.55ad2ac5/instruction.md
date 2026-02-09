# Bug Report

### Describe the bug

The logger's `report()` function is not returning the correct reporting method. It always returns the 'ignore' method regardless of what `reportingSeverity` value is passed in.

### Reproduction

```js
import logger from '@docusaurus/logger';

// Try to report with 'error' severity
const errorReporter = logger.report('error');

// Expected: should use the error reporting method
// Actual: uses the ignore method instead
errorReporter('This should be an error');

// Same issue with other severity levels
const warnReporter = logger.report('warn');
warnReporter('This should be a warning'); // Also ignored
```

### Expected behavior

The `report()` function should return the appropriate reporting method based on the `reportingSeverity` parameter:
- `'error'` should return the error reporting method
- `'warn'` should return the warn reporting method  
- `'ignore'` should return the ignore method
- `'throw'` should return the throw method

Currently all severity levels are being treated as 'ignore', which means error and warning messages are being silently suppressed.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
