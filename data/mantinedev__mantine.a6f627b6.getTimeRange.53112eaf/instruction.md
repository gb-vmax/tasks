# Bug Report

### Describe the bug

The `getTimeRange` utility function is generating incorrect time ranges. When I specify a start time, end time, and interval, the resulting array is missing time slots and the intervals between times are doubled.

### Reproduction

```js
import { getTimeRange } from '@mantine/dates';

const result = getTimeRange({
  startTime: '09:00',
  endTime: '17:00',
  interval: '00:30'
});

console.log(result);
// Expected: ['09:00', '09:30', '10:00', '10:30', ..., '16:30', '17:00']
// Actual: ['09:00', '10:00', '11:00', '12:00', ..., '16:00'] (missing many slots and end time)
```

### Expected behavior

The function should:
1. Include all time slots from start to end time based on the specified interval
2. Include the end time if it aligns with the interval
3. Generate slots at the correct interval (e.g., every 30 minutes if interval is '00:30')

Currently, it's skipping time slots and the intervals appear to be doubled (e.g., 1 hour intervals instead of 30 minutes).

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
