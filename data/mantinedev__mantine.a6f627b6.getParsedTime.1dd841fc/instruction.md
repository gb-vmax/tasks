# Bug Report

### Describe the bug

The TimePicker component is behaving unexpectedly when handling empty time strings. When an empty string is passed, the component attempts to parse it using `splitTimeString()` which is unnecessary and causes issues with the time format handling.

Additionally, there seems to be a problem with the 24-hour format where the time is being incorrectly converted to 12-hour format even when `format` is not set to `'12h'`.

### Reproduction

```js
import { getParsedTime } from '@mantine/dates';

// Case 1: Empty string with 12h format
const result1 = getParsedTime({ 
  time: '', 
  format: '12h',
  amPmLabels: { am: 'AM', pm: 'PM' }
});
// Expected: { hours: null, minutes: null, seconds: null, amPm: null }
// Actual: Tries to parse empty string and returns unexpected values

// Case 2: 24-hour format
const result2 = getParsedTime({ 
  time: '14:30:00', 
  format: '24h',
  amPmLabels: { am: 'AM', pm: 'PM' }
});
// Expected: { hours: '14', minutes: '30', seconds: '00', amPm: null }
// Actual: Time gets converted to 12-hour format incorrectly
```

### Expected behavior

1. Empty time strings should return null values for all fields without attempting to parse
2. When format is set to `'24h'`, the time should remain in 24-hour format and not be converted to 12-hour format

### System Info

- @mantine/dates version: latest
- Browser: All browsers affected

---
Repository: /testbed
