# Bug Report

### Describe the bug

The `secondsToTime` function in TimePicker is returning incorrect values for minutes and seconds. When converting seconds to time format, the minutes and seconds are calculated incorrectly, causing the displayed time to be wrong.

### Reproduction

```js
import { secondsToTime } from '@mantine/dates';

// Convert 3661 seconds (should be 1 hour, 1 minute, 1 second)
const result = secondsToTime(3661);
console.log(result);
// Expected: { timeString: "01:01:01", hours: 1, minutes: 1, seconds: 1 }
// Actual: Wrong values for minutes and seconds
```

### Steps to reproduce:
1. Use the `secondsToTime` utility function with any value
2. Check the returned minutes and seconds values
3. Notice they don't match the expected time conversion

### Expected behavior

When converting seconds to time format, the function should correctly calculate:
- Hours: total seconds divided by 3600
- Minutes: remaining seconds (after hours) divided by 60
- Seconds: remaining seconds after hours and minutes

For example, 3661 seconds should convert to 1 hour, 1 minute, and 1 second.

### System Info
- @mantine/dates version: latest
- Browser: N/A (utility function)

---
Repository: /testbed
