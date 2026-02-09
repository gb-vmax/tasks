# Bug Report

### Describe the bug

When logging Date objects using the logger, they are being converted to JSON strings instead of being formatted as UTC date strings. The logger appears to be treating Date objects as regular objects and stringifying them with `JSON.stringify()` rather than using the proper date formatting.

### Reproduction

```js
import logger from '@docusaurus/logger';

const now = new Date('2024-01-15T10:30:00Z');

// This outputs a JSON string representation instead of a formatted date
logger.info`Current time: ${now}`;

// Expected: "Current time: Mon, 15 Jan 2024 10:30:00 GMT"
// Actual: "Current time: {}"
```

### Expected behavior

Date objects should be formatted as UTC strings (e.g., "Mon, 15 Jan 2024 10:30:00 GMT") when logged, not converted to JSON. This is the standard behavior for displaying dates in logs and makes them much more readable.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
