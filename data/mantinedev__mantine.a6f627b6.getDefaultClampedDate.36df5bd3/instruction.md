# Bug Report

### Describe the bug

The date clamping logic in date pickers seems to be broken. When I set a `minDate` prop, dates that should be valid are getting clamped to the minimum date instead of being left alone.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

// Set minDate to January 1, 2023
const minDate = new Date(2023, 0, 1);

// Try to use a date in the future (e.g., June 15, 2024)
// Expected: June 15, 2024 should be valid since it's after minDate
// Actual: The date gets clamped to January 1, 2023

<DatePicker minDate={minDate} />
```

When the current date is after the `minDate`, it's being incorrectly clamped to `minDate`. This doesn't make sense - dates after the minimum should be perfectly valid.

Also noticed that when both `minDate` and `maxDate` are set, the fallback behavior seems off. It's returning `maxDate` even when today's date should be valid.

### Expected behavior

- If today's date is after `minDate`, it should remain as today's date (not be clamped)
- If today's date is before `minDate`, it should be clamped to `minDate`  
- If today's date is after `maxDate`, it should be clamped to `maxDate`
- The fallback should return today's date, not `maxDate`

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
