# Bug Report

### Describe the bug

The logger's `success()` method is not working correctly when called with string messages. It seems to be treating regular strings as template strings and attempting interpolation, which causes unexpected behavior.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This doesn't work as expected
logger.success('Build completed successfully');

// The message gets processed incorrectly
logger.success('Deployment finished');
```

When calling `success()` with a simple string message (no template literals or interpolation values), the output is malformed or doesn't appear correctly.

### Expected behavior

The logger should output the success message with the green `[SUCCESS]` prefix followed by the message text. Simple string messages should be displayed as-is without any interpolation attempts.

```
[SUCCESS] Build completed successfully
[SUCCESS] Deployment finished
```

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
