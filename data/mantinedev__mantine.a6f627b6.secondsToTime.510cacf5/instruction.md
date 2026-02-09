# Bug Report

### Describe the bug

The `secondsToTime` utility function in the TimePicker component is producing incorrect time conversions. When converting seconds back to time format, the minutes calculation is wrong - it's not properly accounting for the hours component.

### Reproduction

```js
import { secondsToTime } from '@mantine/dates';

// Converting 3661 seconds (1 hour, 1 minute, 1 second)
const result = secondsToTime(3661);
console.log(result.timeString); 
// Expected: "01:01:01"
// Actual: "01:61:01"

// Converting 7265 seconds (2 hours, 1 minute, 5 seconds)
const result2 = secondsToTime(7265);
console.log(result2.timeString);
// Expected: "02:01:05"
// Actual: "02:121:05"
```

The minutes value is including the total minutes instead of just the remaining minutes after hours are accounted for. This causes values like 61 or 121 minutes to appear in the output string instead of the correct 0-59 range.

### Expected behavior

The function should correctly convert seconds to HH:MM:SS format where:
- Hours = total seconds / 3600
- Minutes = remaining seconds after hours / 60 (should be 0-59)
- Seconds = remaining seconds after minutes (should be 0-59)

### System Info
- @mantine/dates version: latest
- Browser: Any

---
Repository: /testbed
