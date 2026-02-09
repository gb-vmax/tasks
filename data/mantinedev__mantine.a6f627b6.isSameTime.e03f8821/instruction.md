# Bug Report

### Describe the bug

The `isSameTime` utility function in the TimePicker component is returning incorrect results when comparing times. It seems to be matching times that are clearly different, leading to unexpected behavior in time selection.

### Reproduction

```js
import { isSameTime } from '@mantine/dates';

// These should NOT be considered the same time, but they are
const result1 = isSameTime({
  time: new Date('2024-01-01 10:30:00'),
  compare: new Date('2024-01-01 15:20:00'),
  withSeconds: false
});
console.log(result1); // Returns true, but should be false

// Also happening with seconds enabled
const result2 = isSameTime({
  time: new Date('2024-01-01 10:30:45'),
  compare: new Date('2024-01-01 10:00:00'),
  withSeconds: true
});
console.log(result2); // Returns true, but should be false
```

### Expected behavior

The function should only return `true` when both times have the same hours AND minutes (and seconds if `withSeconds` is enabled). Different times should not be considered equal.

For example:
- `10:30` should NOT equal `15:20`
- `10:30:45` should NOT equal `10:00:00`

### System Info
- @mantine/dates version: latest
- React version: 18.x

This is causing issues in my time picker where selecting different times doesn't properly update the selected state.

---
Repository: /testbed
