# Bug Report

### Describe the bug

When logging Date objects using the logger, they are now being converted to strings in an unexpected format instead of the UTC string format that was previously used.

### Reproduction

```js
import logger from '@docusaurus/logger';

const date = new Date('2024-01-15T10:30:00Z');
logger.info`Current date: ${date}`;
```

### Expected behavior

The date should be logged in UTC string format (e.g., `Mon, 15 Jan 2024 10:30:00 GMT`), but instead it's being converted using the default `String()` conversion which produces a different format.

This affects any code that relies on the logger to output dates in a consistent UTC format for debugging or logging purposes.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
