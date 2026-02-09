# Bug Report

### Describe the bug

When using the TimePicker component with 24-hour format and `withSeconds` enabled, the component returns an invalid state even when seconds value is `null`. This prevents the time picker from displaying valid time strings in 24-hour format when seconds aren't set yet.

### Reproduction

```js
import { getTimeString } from '@mantine/dates';

// This should return a valid time string but returns invalid instead
const result = getTimeString({
  hours: 14,
  minutes: 30,
  seconds: null,
  format: '24h',
  withSeconds: true,
  amPm: null
});

console.log(result);
// Expected: { valid: true, value: '14:30:00' } or similar
// Actual: { valid: false, value: '' }
```

### Expected behavior

In 24-hour format, the time picker should still return a valid time string even when `seconds` is null and `withSeconds` is true. The validation for null seconds should only apply to 12-hour format where `amPm` is also required.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
