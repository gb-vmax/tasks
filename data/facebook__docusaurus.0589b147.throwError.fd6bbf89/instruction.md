# Bug Report

### Describe the bug

The `throwError` function is not correctly handling template string interpolation. When calling `throwError` with interpolation values, the error message is not being formatted properly - it seems like the logic for when to use `stringify` vs `interpolate` got reversed.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This should throw an error with interpolated values
logger.throwError`Expected ${5} but got ${3}`;

// The error message doesn't include the interpolated values
// Instead it just shows the raw template string
```

### Expected behavior

When using template literal syntax with `throwError`, the interpolated values should be included in the error message. For example:
- `throwError\`Expected ${5} but got ${3}\`` should throw an error with message "Expected 5 but got 3"
- `throwError('simple message')` should throw an error with message "simple message"

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
