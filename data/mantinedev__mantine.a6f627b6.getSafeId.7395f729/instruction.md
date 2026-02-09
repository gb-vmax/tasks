# Bug Report

### Describe the bug

The `getSafeId` utility function crashes with a `TypeError` when passed non-string values like `null` or `undefined`. The function tries to call `.trim()` on the value before checking if it's a string, which causes the error.

### Reproduction

```js
import { getSafeId } from '@mantine/core';

const generateId = getSafeId('mantine', 'ID is required');

// This throws: TypeError: value.trim is not a function
generateId(null);

// This also throws the same error
generateId(undefined);
```

### Expected behavior

The function should throw the custom error message ("ID is required" in this case) instead of crashing with a TypeError. The type check should happen before trying to call string methods on the value.

### System Info
- @mantine/core version: latest
- Node version: 18.x

---
Repository: /testbed
