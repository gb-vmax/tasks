# Bug Report

### Describe the bug

The YearsList component is showing incorrect keyboard navigation behavior. When tabbing through the year picker, disabled years are receiving focus instead of being skipped, and the initial focused year seems to be wrong.

### Reproduction

```jsx
import { YearPicker } from '@mantine/dates';

function Demo() {
  const minDate = new Date(2020, 0, 1);
  const maxDate = new Date(2025, 11, 31);
  
  return (
    <YearPicker 
      minDate={minDate}
      maxDate={maxDate}
      defaultDate={new Date(2023, 0, 1)}
    />
  );
}
```

Steps to reproduce:
1. Render a YearPicker with min/max date constraints
2. Press Tab to focus the year picker
3. Notice that disabled years (outside the min/max range) can receive focus
4. The first year that receives focus is not the expected enabled year

### Expected behavior

- Only enabled years (within the min/max date range and not explicitly disabled) should be focusable when navigating with keyboard
- The first focusable year should be the earliest enabled year, or the selected/current year if available

### System Info

- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
