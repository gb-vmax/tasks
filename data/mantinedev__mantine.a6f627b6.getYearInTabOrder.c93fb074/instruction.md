# Bug Report

### Describe the bug

When using the YearsList component, the keyboard navigation (tab order) is selecting disabled years instead of enabled ones. The tab focus lands on years that should not be selectable based on the `minDate`, `maxDate`, or custom `getYearControlProps` disabled state.

### Reproduction

```jsx
import { YearsList } from '@mantine/dates';

function Demo() {
  const minDate = new Date(2020, 0, 1);
  const maxDate = new Date(2025, 11, 31);
  
  return (
    <YearsList
      minDate={minDate}
      maxDate={maxDate}
      decade={new Date(2020, 0, 1)}
    />
  );
}

// When tabbing through the years, focus goes to years outside the min/max range
// instead of focusing on the first enabled year within the range
```

### Expected behavior

When tabbing into the YearsList component, the focus should land on the first enabled (non-disabled) year. Years that are disabled by `minDate`, `maxDate`, or through `getYearControlProps` should be skipped in the tab order.

Currently, it seems like the logic is inverted - disabled years are being included in the tab order while enabled years are being filtered out.

### System Info

- @mantine/dates version: latest
- Browser: Chrome/Firefox/Safari

---
Repository: /testbed
