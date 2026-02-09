# Bug Report

### Describe the bug

I'm experiencing an issue with the TimePicker component when displaying times in 12-hour format. The conversion from 24-hour to 12-hour format is producing incorrect results for certain hours.

### Reproduction

```js
// When setting a time with hours = 12 (noon)
const time = { hours: 12, minutes: 30, seconds: 0 };
// Expected: 12:30 PM
// Actual: Shows incorrect hour or AM/PM label

// Similarly, midnight (00:00) is also affected
const midnightTime = { hours: 0, minutes: 0, seconds: 0 };
// Expected: 12:00 AM
// Actual: Shows wrong conversion
```

### Expected behavior

- 12:00 (noon) should display as **12:00 PM**
- 00:00 (midnight) should display as **12:00 AM**
- Hours 1-11 should display as **1-11 AM**
- Hours 13-23 should display as **1-11 PM**

The 12-hour format conversion should follow standard conventions where:
- Midnight is 12:00 AM
- Noon is 12:00 PM
- Hours wrap around correctly

### System Info

- @mantine/dates: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
