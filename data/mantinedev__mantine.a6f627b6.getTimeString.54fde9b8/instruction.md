# Bug Report

### Describe the bug

When using the TimePicker component with `format="24h"`, the component returns an invalid state even when the time is properly set. This seems to happen when the time is valid but the validation logic incorrectly checks for `amPm` value in 24-hour format.

### Reproduction

```jsx
import { TimePicker } from '@mantine/dates';

// Set up TimePicker with 24h format
<TimePicker 
  format="24h"
  value={new Date()}
/>

// Try to get the time value - it returns invalid even though the time is set correctly
// The internal getTimeString function returns { valid: false, value: '' }
```

When using 24-hour format, the time picker should not require an AM/PM value, but it seems like the validation is checking for it anyway.

### Expected behavior

The TimePicker should correctly validate times in 24-hour format without requiring an AM/PM designation. The `getTimeString` function should return `{ valid: true, value: '14:30' }` for a valid 24-hour time like 2:30 PM.

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest

---
Repository: /testbed
