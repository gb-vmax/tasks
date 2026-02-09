# Bug Report

### Describe the bug

The logger's `warn()` function is not displaying warning messages correctly when called with a simple string message and no interpolation values. Instead of showing the actual warning message, it appears to be showing something else or behaving unexpectedly.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This doesn't display the warning message as expected
logger.warn('This is a warning message');

// The message that should appear is not being shown
logger.warn('Configuration file is missing');
```

### Expected behavior

When calling `logger.warn()` with a single string argument, the warning message should be displayed in the console with the `[WARNING]` prefix. The actual message content should be visible to the user.

For example:
```
[WARNING] This is a warning message
[WARNING] Configuration file is missing
```

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
