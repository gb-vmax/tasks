# Bug Report

### Describe the bug

I'm encountering an issue with `getSafeId` utility function when passing non-string values. The function throws a cryptic error instead of properly validating the input type first.

### Reproduction

```js
import { getSafeId } from '@mantine/core';

const safeId = getSafeId('my-uid', 'Invalid ID provided');

// This crashes with "value.trim is not a function" 
// instead of the expected error message
safeId(null);
safeId(undefined);
safeId(123);
```

### Expected behavior

The function should check if the value is a string before calling `.trim()` on it, and throw the custom error message when a non-string value is provided. Currently it tries to call `.trim()` on non-string values which causes a TypeError.

### System Info
- @mantine/core version: latest
- Node version: 18.x

---
Repository: /testbed
