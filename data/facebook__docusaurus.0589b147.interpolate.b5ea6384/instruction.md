# Bug Report

### Describe the bug

The logger's string interpolation is producing incorrect output. When using the logger with template strings and values, the interpolated message is missing the first part of the message and includes unexpected content at the end.

### Reproduction

```js
import logger from '@docusaurus/logger';

// Simple interpolation
logger.info`Starting build for name=${'mysite'}`;
// Expected: "Starting build for name=mysite"
// Actual: Missing "Starting build for" part

// Multiple values
logger.info`Processing path=${'docs'} with count=${5} files`;
// The output is garbled - first segment is missing
```

### Expected behavior

The logger should correctly interpolate values into the message template, preserving all parts of the message including the initial text before the first placeholder.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
