# Bug Report

### Describe the bug

When using the MonthsList component, keyboard navigation seems to focus on the wrong month. Instead of focusing on the first available month when there's no selected or current month, it appears to be focusing on the last month in the list.

### Reproduction

```tsx
import { MonthsList } from '@mantine/dates';

// Create a MonthsList without a selected month or current month in view
<MonthsList 
  year={new Date(2025, 0, 1)}
  getMonthControlProps={(month) => ({
    disabled: month.getMonth() < 3 // disable first 3 months
  })}
/>
```

When tabbing into the component, the focus goes to December (last month) instead of April (first enabled month).

### Expected behavior

When there's no selected month and the current month is not in the enabled range, the component should focus on the **first** enabled month in the list, not the last one. This would provide a more intuitive keyboard navigation experience.

### System Info
- @mantine/dates version: latest
- Browser: tested on Chrome and Firefox

---
Repository: /testbed
