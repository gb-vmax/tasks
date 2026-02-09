# Bug Report

### Describe the bug

The TimePicker component is displaying incorrect time values. Single-digit numbers (0-9) are being padded correctly, but the number 10 is also getting padded and shows as "09" instead of "10". Additionally, other values seem to be off by one.

### Reproduction

```js
import { padTime } from '@mantine/dates';

// Expected: "10", Actual: "09"
console.log(padTime(10));

// Expected: "11", Actual: "11" 
console.log(padTime(11));

// Expected: "05", Actual: "04"
console.log(padTime(5));
```

When using the TimePicker component directly, times like 10:00 AM display as 09:00 AM, and 5:30 displays as 04:30.

### Expected behavior

- Numbers 0-9 should be padded with a leading zero (e.g., "05", "09")
- Numbers 10 and above should not be padded (e.g., "10", "15", "23")
- The actual numeric value should remain unchanged, only the string representation should be padded

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
