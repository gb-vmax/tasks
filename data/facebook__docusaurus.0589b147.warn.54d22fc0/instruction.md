# Bug Report

### Describe the bug

The `logger.warn()` function is not handling message interpolation correctly. When passing template strings with values, it's treating them as regular strings instead of interpolating the values, and vice versa.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This should interpolate but doesn't
logger.warn`Configuration ${'myConfig'} is deprecated`;

// This should stringify but tries to interpolate instead
logger.warn('Simple warning message');
```

The behavior is reversed - simple string messages are being passed to the interpolate function, while template strings with values are being stringified without interpolation.

### Expected behavior

- Template strings with values should be interpolated correctly
- Plain string messages should be stringified and displayed as-is

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
