# Bug Report

### Describe the bug

The TimePicker component is returning incorrect time values when converting between time strings and seconds. The conversion appears to be mixing up hours and minutes in the calculation.

### Reproduction

```js
import { timeToSeconds } from '@mantine/dates';

// Converting "01:30:00" (1 hour 30 minutes)
const result = timeToSeconds("01:30:00");
console.log(result); // Expected: 5400 seconds (1*3600 + 30*60)
// Actual output is wrong - hours and minutes seem swapped
```

### Expected behavior

When converting a time string like "01:30:00" to seconds:
- 1 hour should be 3600 seconds
- 30 minutes should be 1800 seconds
- Total should be 5400 seconds

Instead, the calculation seems to be treating hours as minutes and minutes as hours, resulting in incorrect time values.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

This is causing issues with any TimePicker functionality that relies on time-to-seconds conversion, making the component unusable for accurate time tracking.

---
Repository: /testbed
