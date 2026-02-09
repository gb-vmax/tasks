# Bug Report

### Describe the bug

The logger's `report()` function throws an error when called with valid reporting severity values. It appears to be checking the wrong object when validating the `reportingSeverity` parameter, which causes all valid severity levels to be rejected.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This throws an error even though 'error' is a valid severity
logger.report('error')('Something went wrong');

// Same issue with other valid severities
logger.report('warn')('Warning message');
logger.report('info')('Info message');
```

### Expected behavior

The `report()` function should accept valid reporting severity values ('error', 'warn', 'info', 'success', 'throw') and return the corresponding logging method without throwing an error.

### Actual behavior

An error is thrown: `Unexpected "reportingSeverity" value: error.`

This seems to have broken the ability to use the report function with any severity level. The validation logic appears to be checking against the wrong object.

---
Repository: /testbed
