# Bug Report

### Describe the bug

The `logger.info()` function is not handling string interpolation correctly. When passing a template string with values, it seems to be treating it as a plain string instead of interpolating the values. Conversely, when passing a simple string without values, it's trying to interpolate it which causes unexpected behavior.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This should interpolate but doesn't work correctly
logger.info`Processing ${count} files`;

// This should just print the string but behaves unexpectedly
logger.info('Simple message');
```

### Expected behavior

- When using template literals with values (e.g., `` logger.info`text ${value}` ``), the values should be properly interpolated into the message
- When passing a plain string without values, it should just stringify and display the message as-is

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
