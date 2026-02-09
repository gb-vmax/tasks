# Bug Report

### Describe the bug

The YearsList component is not focusing on the correct year when navigating with keyboard. Instead of focusing on enabled years, it seems to be focusing on disabled years, and when no specific year should be selected, it focuses on the last year in the list instead of the first one.

### Reproduction

```jsx
import { YearsList } from '@mantine/dates';

function Demo() {
  return (
    <YearsList
      decade={new Date(2020, 0, 1)}
      minDate={new Date(2022, 0, 1)}
      maxDate={new Date(2028, 0, 1)}
    />
  );
}
```

When tabbing into the YearsList component:
1. The focus goes to a disabled year instead of an enabled one
2. If there's no selected year, the last year in the range gets focused instead of the first enabled year

### Expected behavior

- The component should only allow tabbing to enabled (non-disabled) years
- When no year is selected, the first enabled year should receive focus by default
- Disabled years should be skipped in the tab order

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox/Safari

---
Repository: /testbed
