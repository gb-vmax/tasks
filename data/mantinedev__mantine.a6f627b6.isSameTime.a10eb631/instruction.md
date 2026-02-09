# Bug Report

### Describe the bug

The `isSameTime` utility function in the TimePicker component is not correctly comparing time values. When comparing two times, it returns `true` even when the times are clearly different, and sometimes returns `false` when they should be the same.

### Reproduction

```js
import { isSameTime } from '@mantine/dates';

// This returns true even though times are different
const result1 = isSameTime({
  time: new Date('2024-01-01 10:30:00'),
  compare: new Date('2024-01-01 15:45:00'),
  withSeconds: false
});
console.log(result1); // Expected: false, Actual: true (if hours match OR minutes match)

// This returns false even though times are the same
const result2 = isSameTime({
  time: new Date('2024-01-01 10:30:00'),
  compare: new Date('2024-01-01 10:30:00'),
  withSeconds: false
});
console.log(result2); // Expected: true, Actual: false (because minutes must NOT match?)

// With seconds enabled, behavior is also incorrect
const result3 = isSameTime({
  time: new Date('2024-01-01 10:00:00'),
  compare: new Date('2024-01-01 15:30:45'),
  withSeconds: true
});
console.log(result3); // Returns true if ANY component matches instead of ALL
```

### Expected behavior

The function should return `true` only when ALL time components (hours AND minutes, and seconds if `withSeconds` is true) match between the two times. It should return `false` if any component is different.

### System Info
- @mantine/dates version: latest
- Node: 18.x

---
Repository: /testbed
