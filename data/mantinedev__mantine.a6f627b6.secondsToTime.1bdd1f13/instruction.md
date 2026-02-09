# Bug Report

### Describe the bug

I'm experiencing an issue with the `secondsToTime` function in the TimePicker component. When converting seconds back to time format, the minutes calculation seems incorrect. 

For example, when I pass in a value like 3661 seconds (which should be 1 hour, 1 minute, and 1 second), the output shows the wrong minutes value.

### Reproduction

```js
import { secondsToTime } from '@mantine/dates';

// Convert 3661 seconds (should be 01:01:01)
const result = secondsToTime(3661);
console.log(result.timeString); // Expected: "01:01:01", but getting wrong output

// Another example with 7325 seconds (should be 02:02:05)
const result2 = secondsToTime(7325);
console.log(result2.timeString); // Expected: "02:02:05", but getting wrong output
```

### Expected behavior

The function should correctly convert seconds to hours, minutes, and seconds format. For 3661 seconds, it should return "01:01:01" (1 hour, 1 minute, 1 second).

### System Info

- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
