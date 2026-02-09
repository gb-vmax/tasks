# Bug Report

### Describe the bug

When using the MonthsList component with `minDate` and `maxDate` props, the month selection behavior is completely broken. All months are appearing as disabled/selectable when they shouldn't be, making the component unusable.

### Reproduction

```jsx
import { MonthsList } from '@mantine/dates';

function Demo() {
  const minDate = new Date(2024, 0, 1); // January 2024
  const maxDate = new Date(2024, 11, 31); // December 2024
  
  return (
    <MonthsList
      minDate={minDate}
      maxDate={maxDate}
    />
  );
}
```

With this setup:
- When both `minDate` and `maxDate` are provided, ALL months become disabled (even valid ones within the range)
- The `minDate` itself is also disabled when it should be selectable
- Without `minDate` or `maxDate`, months that should be unrestricted are now being disabled

### Expected behavior

- Months before `minDate` should be disabled
- Months after `maxDate` should be disabled  
- Months within the range (including `minDate` and `maxDate` themselves) should be selectable
- When no `minDate`/`maxDate` is provided, all months should be selectable

### System Info

- @mantine/dates version: latest
- React version: 18.x

This is blocking our date picker implementation. Any help would be appreciated!

---
Repository: /testbed
