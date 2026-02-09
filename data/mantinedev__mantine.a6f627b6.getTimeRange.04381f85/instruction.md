# Bug Report

### Describe the bug

I'm experiencing an issue with the `getTimeRange` function in the TimePicker component. When generating a time range with a specific start time, end time, and interval, the function is producing unexpected results. It seems like the intervals are not being calculated correctly and some time values are being skipped.

### Reproduction

```js
import { getTimeRange } from '@mantine/dates';

const result = getTimeRange({
  startTime: '09:00',
  endTime: '17:00',
  interval: '01:00'
});

console.log(result);
// Expected: ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']
// Actual: ['09:00', '11:00', '13:00', '15:00', '17:00'] (or similar skipped values)
```

The function appears to be skipping intervals after the first one. For example, with a 1-hour interval starting at 09:00, it jumps from 09:00 directly to 11:00 instead of 10:00.

### Expected behavior

The function should generate a sequential list of times from startTime to endTime with consistent intervals. Each time value should be exactly `interval` apart from the previous one.

### System Info
- @mantine/dates version: latest
- Node version: 18.x

---
Repository: /testbed
