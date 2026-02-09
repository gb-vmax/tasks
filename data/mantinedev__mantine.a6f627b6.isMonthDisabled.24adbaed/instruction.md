# Bug Report

### Describe the bug

When using the MonthsList component with `minDate` or `maxDate` props, the months that match the exact min/max dates are being incorrectly disabled. For example, if I set `minDate` to January 2024, January 2024 itself becomes disabled and unselectable, even though it should be the first selectable month.

### Reproduction

```jsx
import { MonthsList } from '@mantine/dates';

// Set minDate to January 2024
const minDate = new Date(2024, 0, 1); // January 2024

<MonthsList minDate={minDate} />
```

In this case, January 2024 is disabled even though it's the minimum allowed date. The same issue occurs with `maxDate` - the exact month specified as the maximum is also disabled.

### Expected behavior

The month specified in `minDate` should be selectable (enabled), and all months before it should be disabled. Similarly, the month specified in `maxDate` should be selectable, and all months after it should be disabled.

For example:
- If `minDate` is January 2024, then January 2024 and later months should be enabled
- If `maxDate` is December 2024, then December 2024 and earlier months should be enabled

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest

---
Repository: /testbed
