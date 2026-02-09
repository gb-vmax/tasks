# Bug Report

### Describe the bug

The YearsList component is not focusing on the correct year when navigating with keyboard. When no year is selected, the component should focus on the current year by default, but it's focusing on the next year instead. Also, disabled years are being included in the tab order when they should be excluded.

### Reproduction

```tsx
import { YearsList } from '@mantine/dates';

function Demo() {
  return (
    <YearsList
      decade={new Date(2020, 0, 1)}
      getYearControlProps={(year) => ({
        disabled: year.getFullYear() === 2023
      })}
    />
  );
}
```

Steps to reproduce:
1. Render a YearsList component without any selected year
2. Tab into the component
3. The focus goes to next year (2025) instead of current year (2024)
4. Years that are explicitly disabled via `getYearControlProps` are still focusable

### Expected behavior

- When no year is selected, keyboard navigation should focus on the current year
- Years marked as disabled through `getYearControlProps` should not be included in the tab order

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
