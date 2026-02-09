# Bug Report

### Describe the bug

The date clamping logic in date picker components is not working correctly. When today's date falls outside the allowed min/max range, it returns the wrong boundary date.

### Reproduction

```js
import { getDefaultClampedDate } from '@mantine/dates';

// Case 1: Today is before minDate
const minDate = new Date('2024-12-01');
const result1 = getDefaultClampedDate({ 
  minDate, 
  timezone: null 
});
// Returns today's date instead of minDate

// Case 2: Today is after maxDate  
const maxDate = new Date('2023-01-01');
const result2 = getDefaultClampedDate({ 
  maxDate, 
  timezone: null 
});
// Returns today's date instead of maxDate
```

### Expected behavior

When today's date is before `minDate`, the function should return `minDate`.
When today's date is after `maxDate`, the function should return `maxDate`.

Currently it seems to be doing the opposite - the clamping logic appears to be inverted.

### System Info
- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
