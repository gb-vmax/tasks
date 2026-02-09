# Bug Report

### Describe the bug

The `TimePicker` component is not correctly comparing times when checking if two time values are the same. When comparing times with seconds enabled, it's returning true even when the times are completely different. Also, when comparing without seconds, it seems to be returning the opposite result - showing times as different when they're actually the same.

### Reproduction

```js
import { isSameTime } from '@mantine/dates';

// Case 1: With seconds
const result1 = isSameTime({
  time: '10:30:45',
  compare: '10:30:45',
  withSeconds: true
});
// Expected: true, but getting unexpected behavior

// Case 2: Without seconds
const result2 = isSameTime({
  time: '10:30',
  compare: '10:30',
  withSeconds: false
});
// Expected: true, but returns false

// Case 3: Different times without seconds
const result3 = isSameTime({
  time: '10:30',
  compare: '11:45',
  withSeconds: false
});
// Expected: false, but returns true
```

### Expected behavior

- When two times have the same hours, minutes, and seconds (if applicable), `isSameTime` should return `true`
- When times differ in any component, it should return `false`
- The comparison logic should work consistently regardless of whether seconds are included or not

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
