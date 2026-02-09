# Bug Report

### Describe the bug

When using the Month component with keyboard navigation, the tab order logic is not working correctly. The component seems to be selecting the wrong date when determining which date should receive focus on tab.

### Reproduction

```jsx
import { Month } from '@mantine/dates';

function Demo() {
  return (
    <Month
      month={new Date(2024, 0, 1)}
      hideOutsideDates
    />
  );
}
```

Steps to reproduce:
1. Render a Month component with `hideOutsideDates` prop
2. Try to tab into the calendar
3. The focused date is incorrect - it seems to focus on dates that don't match the current date

### Expected behavior

When tabbing into the calendar, the current date (today) should receive focus. If today is not available, the first enabled date in the month should be focused instead.

Currently it appears to be focusing on dates in the past or selecting dates that don't match today's date at all.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
