# Bug Report

### Describe the bug

The logger's `warn` function is displaying warning messages incorrectly. When I pass a template string with interpolated values, it seems to be using the wrong formatting logic - it's treating the message as if it has no values when it actually does have values, and vice versa.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This should interpolate the values but doesn't work correctly
logger.warn`Found ${5} broken links`;

// The output formatting is wrong - values aren't being interpolated properly
```

### Expected behavior

When using template string syntax with the warn function, the interpolated values should be properly inserted into the message. The function should correctly detect when values are provided and format them accordingly.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
