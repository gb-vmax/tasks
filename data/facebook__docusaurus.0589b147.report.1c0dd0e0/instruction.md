# Bug Report

### Describe the bug

The `report()` function in the logger is not respecting the `reportingSeverity` parameter correctly. Regardless of what severity level is passed (e.g., 'error', 'warn', 'throw'), it always returns the same logging method instead of the appropriate one for the specified severity.

### Reproduction

```js
import logger from '@docusaurus/logger';

// All of these should return different reporting methods
// but they all behave the same way
const errorReporter = logger.report('error');
const warnReporter = logger.report('warn');
const throwReporter = logger.report('throw');

// Expected: errorReporter should log as error
// Expected: warnReporter should log as warning  
// Expected: throwReporter should throw
// Actual: All three behave identically
```

### Expected behavior

Each reporting severity level should return its corresponding method:
- `'error'` should return the error logging method
- `'warn'` should return the warn logging method
- `'throw'` should return the throw method
- `'ignore'` should return the success method

Currently all severity levels appear to be mapped to the same output method.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
