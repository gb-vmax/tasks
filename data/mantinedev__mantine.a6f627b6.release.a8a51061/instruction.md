# Bug Report

### Describe the bug

The `patchConsoleWarn.release()` function seems to have an issue where it's not properly restoring the original `console.warn` method. After calling `release()`, the console.warn behavior is broken and doesn't function as expected in subsequent operations.

### Reproduction

```js
import { patchConsoleWarn } from '@mantine-tests/core';

// Patch console.warn
patchConsoleWarn();

// Do some testing...
console.warn('This is patched');

// Release the patch
patchConsoleWarn.release();

// Try to use console.warn again
console.warn('This should work normally');

// Call release again
patchConsoleWarn.release();

// Now console.warn is completely broken
console.warn('This will not work correctly');
```

### Expected behavior

After calling `patchConsoleWarn.release()`, the original `console.warn` should be restored and work normally. Multiple calls to `release()` should be safe and idempotent - they shouldn't break the console.warn functionality.

### System Info
- @mantine/core version: latest
- Node.js version: 18.x

---
Repository: /testbed
