# Bug Report

### Describe the bug

The date picker calendar is not focusing on the correct date when navigating with keyboard. Instead of focusing on the first available date, it seems to be focusing on the last date in the month, and dates that should be excluded are actually being included in the tab order.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function Demo() {
  const excludedDates = [
    new Date(2024, 0, 5),
    new Date(2024, 0, 10),
    new Date(2024, 0, 15)
  ];

  return (
    <DatePicker
      excludeDate={(date) => 
        excludedDates.some(d => d.getTime() === date.getTime())
      }
      minDate={new Date(2024, 0, 1)}
      maxDate={new Date(2024, 0, 31)}
    />
  );
}
```

Steps to reproduce:
1. Open the date picker
2. Try to tab through the calendar dates
3. Notice that excluded dates can be focused/selected
4. The initial focus goes to the wrong date (last instead of first)

### Expected behavior

- Excluded dates should not be focusable
- When tabbing into the calendar, the first available (non-excluded, enabled) date should receive focus
- The tab order should respect the `excludeDate` function

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
