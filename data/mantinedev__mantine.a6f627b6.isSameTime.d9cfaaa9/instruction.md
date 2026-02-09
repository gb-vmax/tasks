# Bug Report

### Describe the bug

The `isSameTime` utility function in the TimePicker component is not correctly comparing time values. When comparing two times, it's returning `true` even when the times are clearly different.

### Reproduction

```js
import { isSameTime } from '@mantine/dates';

// These two times are different but the function returns true
const result1 = isSameTime({
  time: new Date('2024-01-01 10:30:00'),
  compare: new Date('2024-01-01 10:45:00'),
  withSeconds: false
});
console.log(result1); // Expected: false, Actual: true

// With seconds enabled, also returns incorrect results
const result2 = isSameTime({
  time: new Date('2024-01-01 10:30:15'),
  compare: new Date('2024-01-01 11:45:20'),
  withSeconds: true
});
console.log(result2); // Expected: false, Actual: true
```

### Expected behavior

The function should return `true` only when both times have the same hours and minutes (and seconds if `withSeconds` is enabled). It should return `false` when any of the time components differ.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
