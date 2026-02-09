# Bug Report

### Describe the bug

The `TimePicker` component is returning incorrect time values when converting between time strings and seconds. It appears that hours and minutes are being calculated incorrectly, resulting in completely wrong time representations.

### Reproduction

```js
import { timeToSeconds } from '@mantine/dates';

// Converting 1 hour to seconds
const result = timeToSeconds('01:00:00');
console.log(result); // Expected: 3600, Actual: 60

// Converting 1 hour 30 minutes to seconds
const result2 = timeToSeconds('01:30:00');
console.log(result2); // Expected: 5400, Actual: 108060
```

When I try to use the TimePicker with any non-zero hour value, the component behaves strangely and displays/stores incorrect times. For example, setting a time of "02:15:00" results in a completely different value being stored.

### Expected behavior

- `timeToSeconds('01:00:00')` should return `3600` (1 hour = 3600 seconds)
- `timeToSeconds('00:30:00')` should return `1800` (30 minutes = 1800 seconds)
- `timeToSeconds('01:30:45')` should return `5445` (1 hour 30 minutes 45 seconds)

The conversion should follow the standard formula: `hours * 3600 + minutes * 60 + seconds`

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
