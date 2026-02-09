# Bug Report

### Describe the bug

The month picker is not setting the correct tab order when navigating through months. When no month is selected and the current month is not in the list, the tab focus goes to the wrong month instead of the first available month.

### Reproduction

```tsx
import { MonthPickerInput } from '@mantine/dates';

function Demo() {
  return (
    <MonthPickerInput
      minDate={new Date(2025, 0, 1)} // January 2025
      maxDate={new Date(2025, 11, 31)} // December 2025
      // Current month (e.g., December 2024) is not in the range
    />
  );
}
```

Steps to reproduce:
1. Open a month picker with a date range that doesn't include the current month
2. Tab into the month picker
3. Observe which month receives focus

### Expected behavior

When tabbing into the month picker, the first enabled month should receive focus. Currently, it appears to be focusing on the last month in the list instead.

### System Info
- @mantine/dates version: latest
- Browser: Any

---
Repository: /testbed
