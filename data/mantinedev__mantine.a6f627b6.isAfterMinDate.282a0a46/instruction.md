# Bug Report

### Describe the bug

The date picker is not respecting the `minDate` prop correctly. When I set a minimum date, dates that should be selectable (specifically the minDate itself) are being disabled or treated as invalid.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function MyComponent() {
  const minDate = new Date('2024-01-15');
  
  return (
    <DatePicker 
      minDate={minDate}
    />
  );
}
```

When rendered, the date `2024-01-15` (the minDate itself) appears to be disabled or cannot be selected, even though it should be the first valid selectable date. Only dates after the minDate are selectable.

### Expected behavior

The `minDate` should be inclusive - meaning the date specified as `minDate` should be selectable. Currently it seems to be treated as exclusive, where only dates *after* the minDate can be selected.

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
