# Bug Report

### Describe the bug
The TimePicker component is producing incorrect time values when converting time strings to seconds. The conversion seems to be calculating wrong results, particularly noticeable when working with hours and minutes.

### Reproduction
```js
import { timeToSeconds } from '@mantine/dates';

// Expected: 3661 seconds (1 hour + 1 minute + 1 second)
// Actual: incorrect value
const result = timeToSeconds('01:01:01');
console.log(result); // Returns wrong calculation

// Another example:
// Expected: 7200 seconds (2 hours)
// Actual: incorrect value
const result2 = timeToSeconds('02:00:00');
console.log(result2);
```

### Expected behavior
`timeToSeconds('01:01:01')` should return `3661` seconds (1 hour = 3600 seconds, 1 minute = 60 seconds, 1 second = 1 second).

`timeToSeconds('02:00:00')` should return `7200` seconds (2 hours = 7200 seconds).

The function should correctly convert time strings in HH:MM:SS format to total seconds.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
