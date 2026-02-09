# Bug Report

### Describe the bug

I'm experiencing an issue with date clamping behavior in the dates package. When a `maxDate` is provided, the function returns the `maxDate` even when the current date is before it, which seems incorrect.

### Reproduction

```js
import { getDefaultClampedDate } from '@mantine/dates';

const today = new Date('2024-01-15');
const maxDate = new Date('2024-12-31');

// This incorrectly returns maxDate even though today is before maxDate
const result = getDefaultClampedDate({
  maxDate,
  minDate: null,
  timezone: null
});

// Expected: today's date (2024-01-15)
// Actual: maxDate (2024-12-31)
console.log(result);
```

### Expected behavior

The function should only return `maxDate` when the current date is **after** the `maxDate`, not before it. When the current date is within the valid range (after `minDate` and before `maxDate`), it should return the current date.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
