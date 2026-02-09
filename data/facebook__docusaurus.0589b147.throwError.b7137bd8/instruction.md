# Bug Report

### Describe the bug

The `throwError` function is not working correctly when called with a simple string message. Instead of throwing an error with the provided message, it seems to be treating the message incorrectly and producing unexpected error text.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This should throw an error with the message "Something went wrong"
logger.throwError('Something went wrong');

// Expected: Error with message "Something went wrong"
// Actual: Error with garbled/incorrect message
```

When passing a plain string to `throwError`, the error message that gets thrown doesn't match what was passed in. It appears the function is trying to interpolate a regular string as if it were a template string.

### Expected behavior

When calling `throwError` with a simple string message, it should throw an Error with that exact message. Template interpolation should only happen when actually using template strings with values.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
