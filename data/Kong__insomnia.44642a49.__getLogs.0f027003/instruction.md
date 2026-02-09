# Bug Report

### Describe the bug

After a recent update, the logger's `__getLogs()` method is returning `null` instead of an empty object. This is causing issues when code tries to access log entries or iterate over the logs.

### Reproduction

```js
import { logger } from './cli';

// This now returns null instead of {}
const logs = logger.__getLogs();

// Attempting to access properties or iterate fails
console.log(logs.errors); // TypeError: Cannot read property 'errors' of null

// Or when trying to spread or use Object methods
const allLogs = { ...logs }; // TypeError: Cannot convert undefined or null to object
```

### Expected behavior

The `__getLogs()` method should return an empty object `{}` when there are no logs, not `null`. This maintains backward compatibility and prevents null reference errors in consuming code.

### Additional context

This appears to have broken after some changes to how the consola logger is initialized. Code that previously worked fine is now throwing null pointer exceptions.

---
Repository: /testbed
