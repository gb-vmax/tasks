# Bug Report

### Describe the bug

After a recent update, the logger's `report` function with `ignore` severity is throwing unexpected errors when called with arguments. Previously, calling the ignore method would silently do nothing regardless of what was passed to it, but now it's throwing an error.

### Reproduction

```js
const logger = require('@docusaurus/logger');

// Create a reporter with 'ignore' severity
const reporter = logger.report('ignore');

// This now throws an error: "Unexpected argument"
reporter('Some message');
```

### Expected behavior

When using `report('ignore')`, the returned function should silently ignore all calls and arguments, just like it did before. It shouldn't throw errors when messages are passed to it.

### System Info
- Docusaurus logger version: latest
- Node version: 18.x

This is breaking existing code that relies on the ignore reporter to safely suppress certain log messages without having to check if the reporter is in ignore mode before calling it.

---
Repository: /testbed
