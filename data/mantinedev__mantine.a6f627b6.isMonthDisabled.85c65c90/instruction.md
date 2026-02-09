# Bug Report

### Describe the bug

When using the MonthsList component with `minDate` and `maxDate` props, the month selection behavior is completely broken. All months are being disabled when both date boundaries are set, making it impossible to select any month within the valid range.

### Reproduction

```tsx
import { MonthsList } from '@mantine/dates';

function Demo() {
  const minDate = new Date(2023, 0, 1); // January 2023
  const maxDate = new Date(2023, 11, 31); // December 2023
  
  return (
    <MonthsList
      minDate={minDate}
      maxDate={maxDate}
      value={new Date(2023, 5, 1)}
    />
  );
}
```

### Expected behavior

- Months between January 2023 and December 2023 should be selectable
- Months outside this range should be disabled
- The maxDate month itself (December 2023) should be selectable

### Actual behavior

- All months are disabled when both minDate and maxDate are provided
- Cannot select any month even though they fall within the valid range
- The component is completely unusable when date boundaries are set

This makes the component unusable for any scenario where you need to restrict month selection to a specific range.

### System Info

- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
