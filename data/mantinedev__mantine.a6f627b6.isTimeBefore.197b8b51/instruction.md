# Bug Report

### Describe the bug

The `isTimeBefore` function is returning incorrect results when comparing time values. It seems to be inverted - times that should be considered "before" are returning false, and times that should be "after" are returning true.

### Reproduction

```js
import { isTimeBefore } from '@mantine/dates';

// This should return true but returns false
console.log(isTimeBefore('09:00', '10:00')); // Expected: true, Got: false

// This should return false but returns true
console.log(isTimeBefore('15:00', '14:00')); // Expected: false, Got: true

// Edge case: same time
console.log(isTimeBefore('12:00', '12:00')); // Expected: false, Got: true
```

### Expected behavior

`isTimeBefore(value, compareTo)` should return `true` when `value` represents a time that comes before `compareTo`, and `false` otherwise.

For example:
- `isTimeBefore('09:00', '10:00')` should return `true` (9 AM is before 10 AM)
- `isTimeBefore('15:00', '14:00')` should return `false` (3 PM is not before 2 PM)
- `isTimeBefore('12:00', '12:00')` should return `false` (same time)

### System Info

- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
