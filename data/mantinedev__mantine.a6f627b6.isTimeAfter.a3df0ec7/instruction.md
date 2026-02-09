# Bug Report

### Describe the bug

The `isTimeAfter` function in the TimeGrid component is returning incorrect results. When comparing two time values, it's giving the opposite of what's expected - returning `true` when the first time is actually before or equal to the second time, instead of after.

### Reproduction

```js
import { isTimeAfter } from '@mantine/dates';

// This returns true but should return false
console.log(isTimeAfter('10:00', '15:00')); // Expected: false, Actual: true

// This returns false but should return true  
console.log(isTimeAfter('15:00', '10:00')); // Expected: true, Actual: false

// Edge case: equal times
console.log(isTimeAfter('12:00', '12:00')); // Expected: false, Actual: true
```

### Expected behavior

`isTimeAfter(value, compareTo)` should return `true` when `value` is after `compareTo`, and `false` otherwise. Currently it's behaving like an "is before or equal" check instead.

### System Info
- @mantine/dates version: latest
- This seems to affect time-based filtering/validation in TimeGrid components

---
Repository: /testbed
