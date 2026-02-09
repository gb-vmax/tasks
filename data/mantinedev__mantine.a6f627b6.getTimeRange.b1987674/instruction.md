# Bug Report

### Describe the bug

I'm experiencing an issue with the `getTimeRange` function in the TimePicker component. The generated time range is missing the start and end times from the output array.

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
// Actual: ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00']
```

The first time slot (09:00) and the last time slot (17:00) are missing from the array. This breaks time selection when users need to select the exact start or end boundary times.

### Expected behavior

The time range should include both the `startTime` and `endTime` values in the returned array, along with all intervals in between.

### System Info

- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
