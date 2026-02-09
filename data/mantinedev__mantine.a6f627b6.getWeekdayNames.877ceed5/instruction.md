# Bug Report

### Describe the bug

The weekday names row in the calendar component is only showing 6 days instead of 7. One weekday is missing from the display, making the calendar header incomplete.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';

function Demo() {
  return (
    <Calendar 
      locale="en"
      firstDayOfWeek={1} // Monday
    />
  );
}
```

When rendering the calendar, the weekdays row only displays 6 day names instead of the expected 7 (e.g., showing "Mon Tue Wed Thu Fri Sat" but missing Sunday).

### Expected behavior

All 7 weekday names should be displayed in the header row of the calendar, regardless of the `firstDayOfWeek` setting.

### Additional context

This seems to affect all locales and `firstDayOfWeek` configurations. The calendar grid itself shows all 7 columns correctly, but the header labels are incomplete.

---
Repository: /testbed
