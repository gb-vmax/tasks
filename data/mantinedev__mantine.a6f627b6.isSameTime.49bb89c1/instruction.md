# Bug Report

### Describe the bug

The `isSameTime` utility function in the TimePicker component is not correctly comparing time values. When comparing two times, it's returning incorrect results - times that should be considered equal are being marked as different, and vice versa.

### Reproduction

```js
import { isSameTime } from '@mantine/dates';

// Case 1: These times should be equal (same hours and minutes)
const result1 = isSameTime({
  time: new Date(2024, 0, 1, 14, 30, 0),
  compare: new Date(2024, 0, 1, 14, 30, 0),
  withSeconds: false
});
console.log(result1); // Expected: true, but getting false

// Case 2: With seconds enabled, identical times should be equal
const result2 = isSameTime({
  time: new Date(2024, 0, 1, 14, 30, 45),
  compare: new Date(2024, 0, 1, 14, 30, 45),
  withSeconds: true
});
console.log(result2); // Expected: true, but getting false

// Case 3: Different times are incorrectly marked as equal
const result3 = isSameTime({
  time: new Date(2024, 0, 1, 10, 30, 0),
  compare: new Date(2024, 0, 1, 14, 45, 0),
  withSeconds: false
});
console.log(result3); // Expected: false, but getting true
```

### Expected behavior

- When `withSeconds` is false, two times should be considered equal if they have the same hours AND minutes
- When `withSeconds` is true, two times should be considered equal if they have the same hours, minutes, AND seconds
- Times with different values should not be considered equal

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest

This is causing issues in our TimePicker component where selected times aren't being properly highlighted or validated.

---
Repository: /testbed
