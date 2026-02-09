# Bug Report

### Describe the bug

The `isTimeAfter` function is incorrectly treating equal times as "after". When comparing two identical time values, the function returns `true` instead of `false`, which doesn't match the expected behavior of an "after" comparison.

### Reproduction

```js
import { isTimeAfter } from '@mantine/dates';

// This should return false but returns true
console.log(isTimeAfter('10:30', '10:30')); // Expected: false, Actual: true

// This correctly returns true
console.log(isTimeAfter('10:31', '10:30')); // Expected: true, Actual: true

// This correctly returns false
console.log(isTimeAfter('10:29', '10:30')); // Expected: false, Actual: false
```

### Expected behavior

When comparing two equal time values, `isTimeAfter` should return `false` since a time cannot be "after" itself. The function should only return `true` when the first time is strictly greater than the second time.

### System Info

- @mantine/dates version: latest
- Browser: All browsers affected (logic issue)

---
Repository: /testbed
