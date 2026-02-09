# Bug Report

### Describe the bug

The TimePicker component is displaying incorrect time values. When entering or displaying times, the values appear to be off by one for certain numbers, and some single-digit numbers are not being padded correctly with a leading zero.

### Reproduction

```js
// When setting time to 10:30, it displays as 09:30
// When setting time to 11:00, it displays as 10:00
// Single digit times like 5:00 work correctly with padding (05:00)
// But the value 10 specifically seems to get padded when it shouldn't

const time = '10:30';
// Expected display: 10:30
// Actual display: 09:30
```

### Expected behavior

- Times should display exactly as entered
- Single-digit hours/minutes (0-9) should be padded with a leading zero
- Double-digit values (10 and above) should NOT be padded and should display their actual value
- No values should be decremented or modified

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
