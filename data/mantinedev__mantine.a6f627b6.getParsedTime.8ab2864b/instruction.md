# Bug Report

### Describe the bug

The TimePicker component is not handling empty time strings correctly when using 12-hour format. When I clear the input or pass an empty string, the component crashes or behaves unexpectedly instead of returning null values.

### Reproduction

```js
import { getParsedTime } from '@mantine/dates';

// This should return null values but throws an error instead
const result = getParsedTime({
  time: '',
  format: '12h',
  amPmLabels: { am: 'AM', pm: 'PM' }
});

// Expected: { hours: null, minutes: null, seconds: null, amPm: null }
// Actual: Error or incorrect behavior
```

### Expected behavior

When passing an empty time string with 12-hour format, the function should return an object with all null values (`{ hours: null, minutes: null, seconds: null, amPm: null }`), similar to how it works with 24-hour format.

### Additional context

This seems to affect the TimePicker component when users clear the input field while using 12-hour time format. The component should gracefully handle empty inputs regardless of the time format being used.

---
Repository: /testbed
