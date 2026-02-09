# Bug Report

### Describe the bug

The TimePicker component is displaying incorrect AM/PM values and wrong hour conversions when converting from 24-hour to 12-hour format. The AM and PM labels appear to be swapped, and midnight (00:00) is showing as 0 instead of 12.

### Reproduction

```js
// When setting a time in 24-hour format
const timePicker = <TimePicker format="12" value="00:00" />
// Displays: 0:00 PM (expected: 12:00 AM)

const timePicker2 = <TimePicker format="12" value="13:00" />
// Displays: 1:00 AM (expected: 1:00 PM)

const timePicker3 = <TimePicker format="12" value="23:59" />
// Displays: 11:59 AM (expected: 11:59 PM)
```

### Expected behavior

- Times from 00:00-11:59 (24-hour) should display as 12:00 AM - 11:59 AM (12-hour)
- Times from 12:00-23:59 (24-hour) should display as 12:00 PM - 11:59 PM (12-hour)
- Midnight (00:00) should display as 12:00 AM, not 0:00

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest

---
Repository: /testbed
