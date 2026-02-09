# Bug Report

### Describe the bug

The logger's `warn()` function doesn't properly handle template string interpolation. When passing multiple arguments to `logger.warn()`, the interpolation isn't being applied correctly and the output doesn't include the interpolated values.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This doesn't interpolate correctly
logger.warn`Configuration value: ${'test'} is invalid`;

// Expected output: [WARNING] Configuration value: test is invalid
// Actual output: [WARNING] Configuration value: ${0} is invalid (or similar)
```

Another example:
```js
const pluginName = 'my-plugin';
const version = '1.0.0';

logger.warn`Plugin ${pluginName} version ${version} is deprecated`;
// The values aren't being substituted properly
```

### Expected behavior

When using template literal syntax with `logger.warn`, the interpolated values should be properly substituted into the message string.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
