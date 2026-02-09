# Bug Report

### Describe the bug

The TimePicker component is not correctly handling time format conversion. When using 12-hour format, the AM/PM indicator is not being set properly, and when using 24-hour format, it's incorrectly attempting to convert to 12-hour format.

### Reproduction

```js
import { getParsedTime } from '@mantine/dates';

// 12-hour format should include AM/PM but returns null
const result12h = getParsedTime({
  time: '02:30:00',
  format: '12h',
  amPmLabels: { am: 'AM', pm: 'PM' }
});
console.log(result12h.amPm); // Expected: 'AM', Actual: null

// 24-hour format should NOT convert to 12-hour format
const result24h = getParsedTime({
  time: '14:30:00',
  format: '24h',
  amPmLabels: { am: 'AM', pm: 'PM' }
});
// This incorrectly tries to convert to 12-hour format
```

### Expected behavior

- When `format='12h'`, the function should convert the time to 12-hour format and include the appropriate AM/PM indicator
- When `format='24h'`, the function should return the time as-is with `amPm: null` and NOT attempt any 12-hour conversion

### System Info

- @mantine/dates version: latest
- Browser: Any

---
Repository: /testbed
