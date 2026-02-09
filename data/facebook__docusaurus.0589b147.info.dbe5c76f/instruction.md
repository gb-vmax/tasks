# Bug Report

### Describe the bug

The logger's `info()` function is not handling interpolated messages correctly. When passing template values to be interpolated, the output shows the raw message instead of the interpolated result.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This should interpolate the values but doesn't
logger.info`Processing ${5} files in ${10}ms`;

// Expected output: [INFO] Processing 5 files in 10ms
// Actual output: [INFO] Processing ${5} files in ${10}ms (raw template string)
```

Conversely, when calling with a simple string message (no interpolation), the behavior is also incorrect:

```js
logger.info('Simple message');

// This seems to try interpolation when it shouldn't
```

### Expected behavior

- Template literal calls like `logger.info\`text ${value}\`` should properly interpolate the values
- Regular string calls like `logger.info('text')` should display the string as-is without attempting interpolation

### System Info
- Docusaurus version: latest
- Node: 18.x

---
Repository: /testbed
