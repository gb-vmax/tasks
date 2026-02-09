# Bug Report

### Describe the bug

The logger's `success()` method is producing incorrect output when called with template strings vs regular strings. It seems like the logic for determining when to use string interpolation versus regular stringification has been reversed.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This should interpolate the template string but doesn't work correctly
logger.success`Deployed to ${url}`;

// This should stringify the message but behaves unexpectedly
logger.success('Build completed successfully');
```

When using tagged template literals (the backtick syntax with interpolated values), the output doesn't include the interpolated values properly. Conversely, when passing a plain string, it's being treated as a template string when it shouldn't be.

### Expected behavior

- When called as a tagged template literal with interpolated values: `logger.success\`Message ${value}\``, it should properly interpolate and display the values
- When called with a regular string: `logger.success('Message')`, it should just stringify and display the message as-is

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
