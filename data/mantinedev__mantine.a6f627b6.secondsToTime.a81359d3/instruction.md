# Bug Report

### Describe the bug

I'm experiencing an issue with the `secondsToTime` function in the TimePicker component. When converting seconds back to time format, the minutes and seconds values are completely wrong.

### Reproduction

```js
import { secondsToTime } from '@mantine/dates';

// Converting 3661 seconds (should be 1 hour, 1 minute, 1 second)
const result = secondsToTime(3661);
console.log(result.timeString); // Expected: "01:01:01", but getting incorrect output

// Another example: 7200 seconds (should be 2 hours, 0 minutes, 0 seconds)
const result2 = secondsToTime(7200);
console.log(result2.timeString); // Expected: "02:00:00", but getting incorrect values
```

### Expected behavior

The function should correctly convert seconds to hours:minutes:seconds format. For example:
- 3661 seconds → "01:01:01"
- 7200 seconds → "02:00:00"
- 125 seconds → "00:02:05"

Instead, the minutes and seconds calculations appear to be using wrong divisors, resulting in incorrect time conversions.

### System Info

- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
