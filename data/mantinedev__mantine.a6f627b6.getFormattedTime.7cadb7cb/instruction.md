# Bug Report

### Describe the bug

When using `TimeValue` component with 12-hour format, the time is being displayed incorrectly for certain hours. Specifically, 12 PM and 12 AM are showing the wrong AM/PM designation, and the hour conversion seems off.

### Reproduction

```js
// When formatting time in 12-hour format:
getFormattedTime({
  value: '12:00',
  format: '12',
  amPmLabels: { am: 'AM', pm: 'PM' }
})
// Expected: "12:00 PM"
// Actual: "12:00 AM"

getFormattedTime({
  value: '00:00',
  format: '12',
  amPmLabels: { am: 'AM', pm: 'PM' }
})
// Expected: "12:00 AM"
// Actual: incorrect output
```

### Expected behavior

- 12:00 (noon) should display as "12:00 PM"
- 00:00 (midnight) should display as "12:00 AM"
- Hours from 1-11 should show AM
- Hours from 13-23 should convert to 1-11 PM

The 12-hour format conversion isn't handling the edge cases for noon and midnight correctly.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
