# Bug Report

### Describe the bug

The date picker is not respecting the `minDate` prop correctly. Dates that should be selectable (on or after the minimum date) are being disabled, and the boundary behavior seems off by a day or two.

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
1. Set minDate to January 15th, 2024
2. Try to select January 15th (the minimum date itself)
3. The date appears disabled even though it should be selectable
4. Sometimes January 16th is also disabled when it shouldn't be

### Expected behavior

Dates on or after `minDate` should be selectable. The minimum date itself (January 15th in the example) should be clickable and not disabled. Only dates before the minimum should be disabled.

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest
- dayjs version: latest

---
Repository: /testbed
