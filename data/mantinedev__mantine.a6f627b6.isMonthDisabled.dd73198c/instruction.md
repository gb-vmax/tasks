# Bug Report

### Describe the bug

When using the MonthsList component with `minDate` and `maxDate` props, the month selection behavior is completely inverted. Months that should be selectable are disabled, and months that should be disabled are selectable.

### Reproduction

```jsx
import { MonthsList } from '@mantine/dates';

// Set a date range where only months between Jan 2023 and Jun 2023 should be selectable
<MonthsList
  minDate={new Date(2023, 0, 1)}  // January 2023
  maxDate={new Date(2023, 5, 30)}  // June 2023
/>
```

### Expected behavior

- Months from January 2023 to June 2023 should be **enabled** and selectable
- Months before January 2023 should be **disabled**
- Months after June 2023 should be **disabled**

### Actual behavior

- Months from January 2023 to June 2023 are **disabled** (should be enabled)
- Months before January 2023 are **enabled** (should be disabled)
- Months after June 2023 are **enabled** (should be disabled)

The logic appears to be completely backwards. Additionally, if only `minDate` OR `maxDate` is provided (not both), all months become enabled when they should respect the single boundary that was set.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
