# Bug Report

### Describe the bug

When logging Date objects using the logger, they're being converted to JSON strings instead of being formatted as UTC strings. The logger is incorrectly serializing Date objects as `{}` rather than calling their `toUTCString()` method.

### Reproduction

```js
import logger from '@docusaurus/logger';

const now = new Date('2024-01-15T10:30:00Z');

// This logs "{}" instead of the formatted date string
logger.info`Current time: ${now}`;

// Expected output: "Current time: Mon, 15 Jan 2024 10:30:00 GMT"
// Actual output: "Current time: {}"
```

### Expected behavior

Date objects should be formatted using `toUTCString()` to produce human-readable date strings like "Mon, 15 Jan 2024 10:30:00 GMT" instead of being serialized as empty JSON objects.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
