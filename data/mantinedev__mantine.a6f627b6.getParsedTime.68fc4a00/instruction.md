# Bug Report

### Describe the bug

When using the TimePicker component with 24-hour format, the `amPm` property is being returned as `null` instead of an empty string when the time input is empty. This causes inconsistent behavior compared to when an empty string is provided.

Additionally, there seems to be an issue with the parsed time object structure when using 24-hour format with non-empty time values - the conversion logic appears to be applied incorrectly, potentially causing the component to return unexpected data.

### Reproduction

```js
import { getParsedTime } from '@mantine/dates';

// Case 1: Empty time string
const result1 = getParsedTime({ time: '', format: '24' });
console.log(result1.amPm); // Expected: '' but getting null

// Case 2: Valid time in 24-hour format
const result2 = getParsedTime({ time: '14:30', format: '24' });
// The returned object structure seems incorrect
console.log(result2);
```

### Expected behavior

- When `time` is an empty string, `amPm` should be an empty string (`''`) for consistency
- When using 24-hour format with a valid time, the parsed time object should maintain the correct structure without applying 12-hour conversion logic

### System Info

- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
