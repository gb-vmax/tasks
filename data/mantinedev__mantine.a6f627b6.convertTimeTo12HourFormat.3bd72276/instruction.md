# Bug Report

### Describe the bug

When using the TimePicker component with 12-hour format, the conversion from 24-hour to 12-hour time is not working correctly. Specifically, times at noon (12:00 PM) are being displayed incorrectly.

### Reproduction

```js
// When setting time to 12:00 (noon) in 24-hour format
const time = { hours: 12, minutes: 0, seconds: 0 };
// The component displays it incorrectly

// Also, 12:00 AM (midnight) conversion seems broken
const midnight = { hours: 0, minutes: 0, seconds: 0 };
// This also doesn't display as expected
```

### Expected behavior

- 12:00 (noon) in 24-hour format should display as 12:00 PM
- 00:00 (midnight) in 24-hour format should display as 12:00 AM
- Hours between 1-11 should remain the same with AM
- Hours between 13-23 should be converted to 1-11 with PM

Currently the 12-hour conversion is producing incorrect values for noon/midnight times.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
