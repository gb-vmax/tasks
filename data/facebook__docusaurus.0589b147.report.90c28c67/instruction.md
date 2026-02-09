# Bug Report

### Describe the bug

When using the `report()` function with `reportingSeverity: 'ignore'`, I'm getting a runtime error instead of the expected silent behavior. The function is trying to call `ignore` as if it were a function, but it appears to be an empty object instead.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This throws an error
logger.report('ignore')('This should be ignored');
```

The error message is something like "ignore is not a function" or similar.

### Expected behavior

When `reportingSeverity` is set to `'ignore'`, the logger should silently do nothing without throwing any errors. This is useful for conditionally suppressing certain log messages based on configuration.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. The `ignore` option used to work fine for silencing specific warnings in our build process.

---
Repository: /testbed
