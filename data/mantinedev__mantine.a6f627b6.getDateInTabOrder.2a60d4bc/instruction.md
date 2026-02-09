# Bug Report

### Describe the bug

I'm experiencing an issue with keyboard navigation in the Month component when `hideOutsideDates` is enabled. The tab order for dates seems to be incorrect - the focus is going to dates outside the current month instead of staying within the visible month dates.

### Reproduction

```jsx
import { Month } from '@mantine/dates';

function Demo() {
  return (
    <Month
      month={new Date(2024, 0, 1)} // January 2024
      hideOutsideDates={true}
    />
  );
}
```

When tabbing through the calendar:
1. Render a Month component with `hideOutsideDates={true}`
2. Try to navigate using keyboard (tab key)
3. The initial focused date is outside the current month instead of being the first date of the current month

### Expected behavior

When `hideOutsideDates` is true, the tab order should prioritize dates within the current month. The first focusable date should be from the current month being displayed, not from adjacent months that are hidden.

Additionally, the fallback date selection seems backwards - it's selecting the last enabled date instead of the first one, which feels unintuitive for keyboard navigation.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
