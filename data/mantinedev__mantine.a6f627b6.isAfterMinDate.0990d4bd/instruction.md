# Bug Report

### Describe the bug

The date picker is not respecting the `minDate` prop correctly. Dates that should be selectable (on or after the minimum date) are being disabled, and dates that should be disabled (before the minimum date) can sometimes be selected.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function Demo() {
  const minDate = new Date('2024-01-15');
  
  return (
    <DatePicker
      minDate={minDate}
    />
  );
}
```

When testing this:
1. Set a minDate (e.g., January 15, 2024)
2. Try to select January 15 itself - it appears disabled even though it should be selectable
3. The day before minDate (January 14) might be selectable in some cases

### Expected behavior

- Dates on or after `minDate` should be selectable
- Dates before `minDate` should be disabled
- The boundary date (minDate itself) should be included in the selectable range

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
