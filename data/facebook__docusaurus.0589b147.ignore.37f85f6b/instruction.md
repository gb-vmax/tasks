# Bug Report

### Describe the bug

When using the logger with `reportingSeverity: 'ignore'`, passing any argument causes the application to crash with a TypeError. The ignore method should silently discard messages, but instead it's throwing an error when trying to access properties on the argument.

### Reproduction

```js
import logger from '@docusaurus/logger';

// Set reporting severity to ignore
const reportFn = logger.report('ignore');

// This crashes the application
reportFn('Some message');
// TypeError: Cannot read property 'nonExistentProperty' of undefined
```

### Expected behavior

When `reportingSeverity` is set to `'ignore'`, the reporting function should silently ignore all messages without throwing any errors. The function should be a no-op and not attempt to access any properties on the arguments passed to it.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This is blocking our production deployment as we use `reportingSeverity: 'ignore'` in certain environments and the application now crashes whenever a report is triggered.

---
Repository: /testbed
