# Bug Report

### Describe the bug
The `secondsToTime` function in the TimePicker component is returning incorrect values for minutes and seconds. When converting a number of seconds back to time format, the minutes and seconds are calculated incorrectly, resulting in wrong time values being displayed.

### Reproduction
```js
import { secondsToTime } from '@mantine/dates';

// Example 1: Converting 3661 seconds (1 hour, 1 minute, 1 second)
const result1 = secondsToTime(3661);
console.log(result1.timeString); 
// Expected: "01:01:01"
// Actual: incorrect output

// Example 2: Converting 7325 seconds (2 hours, 2 minutes, 5 seconds)
const result2 = secondsToTime(7325);
console.log(result2.timeString);
// Expected: "02:02:05"
// Actual: incorrect output
```

### Expected behavior
The function should correctly convert seconds to hours:minutes:seconds format. For example:
- 3661 seconds should return "01:01:01" (1 hour, 1 minute, 1 second)
- 7325 seconds should return "02:02:05" (2 hours, 2 minutes, 5 seconds)
- 125 seconds should return "00:02:05" (0 hours, 2 minutes, 5 seconds)

### System Info
- @mantine/dates version: latest
- Framework: React

---
Repository: /testbed
