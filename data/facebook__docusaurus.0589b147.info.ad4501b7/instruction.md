# Bug Report

### Describe the bug

The logger's `info()` function is not interpolating template strings correctly. When passing multiple values to be interpolated into a log message, the values are being ignored and only the template string itself is being logged.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This should interpolate the values into the message
logger.info`Processing ${count} files in ${directory}`;

// Expected output: [INFO] Processing 5 files in /src/pages
// Actual output: [INFO] Processing ${count} files in ${directory}
```

The interpolation values are not being substituted into the template string, resulting in the raw template being logged instead of the formatted message.

### Expected behavior

When using tagged template literals with `logger.info`, the interpolated values should be properly substituted into the message string, similar to how console.log handles template literals.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
