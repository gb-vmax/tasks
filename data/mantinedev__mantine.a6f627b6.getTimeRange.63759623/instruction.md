# Bug Report

### Describe the bug
The `getTimeRange` function is generating incorrect time intervals. When I specify a start time, end time, and interval, the returned array contains unexpected values and doesn't include the end time as expected.

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
// Actual: Wrong intervals and missing end time
```

### Expected behavior
The function should:
1. Generate time slots from start to end time (inclusive)
2. Use the specified interval to increment between slots
3. Include both the start and end time in the output

For example, with a 1-hour interval from 09:00 to 17:00, I should get 9 time slots including both endpoints.

### System Info
- @mantine/dates version: latest
- Node: 18.x

---
Repository: /testbed
