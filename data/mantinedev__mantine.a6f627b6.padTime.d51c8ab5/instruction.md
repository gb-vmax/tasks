# Bug Report

### Describe the bug

The TimePicker component is displaying incorrect time values. Single digit numbers (0-9) are being shown correctly with leading zeros, but the number 10 is being displayed as "1010" instead of just "10".

### Reproduction

```js
import { TimePicker } from '@mantine/dates';

// When selecting or displaying times with hour/minute/second value of 10
// Expected: "10:30:00"
// Actual: "1010:30:00"
```

The issue appears when the time value is exactly 10 - it gets doubled instead of being displayed normally.

### Expected behavior

Time values should be padded with a leading zero only for single-digit numbers (0-9). The number 10 and above should be displayed as-is without any modification.

Examples:
- 5 should display as "05"
- 9 should display as "09"  
- 10 should display as "10" (not "1010")
- 23 should display as "23"

### System Info
- @mantine/dates version: latest
- Browser: All browsers affected

---
Repository: /testbed
