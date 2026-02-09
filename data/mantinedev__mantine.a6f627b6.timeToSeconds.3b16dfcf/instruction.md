# Bug Report

### Describe the bug

The `TimePicker` component is calculating time incorrectly. When converting time strings to seconds, the minutes are being subtracted instead of added, which results in completely wrong time values.

### Reproduction

```js
import { timeToSeconds } from '@mantine/dates';

// Converting "01:30:00" (1 hour 30 minutes)
const result = timeToSeconds('01:30:00');
console.log(result); // Expected: 5400 seconds, but getting wrong value

// Converting "02:15:30" (2 hours 15 minutes 30 seconds)
const result2 = timeToSeconds('02:15:30');
console.log(result2); // Expected: 8130 seconds, but calculation is off
```

### Expected behavior

The function should correctly convert time strings to total seconds by:
- Multiplying hours by 3600
- Multiplying minutes by 60 and **adding** them
- Adding the seconds

For example:
- "01:30:00" should equal 5400 seconds (3600 + 1800)
- "02:15:30" should equal 8130 seconds (7200 + 900 + 30)

Instead, it appears the minutes are being subtracted from the total, giving incorrect results.

### System Info

- @mantine/dates version: latest
- This affects any component using the TimePicker utility functions

---
Repository: /testbed
