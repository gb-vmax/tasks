# Bug Report

### Describe the bug

When using the Month component with `hideOutsideDates` enabled, the tab order logic is not working correctly. The component seems to be comparing dates against the wrong reference month, which causes issues with keyboard navigation when dates from outside the current month should be excluded.

### Reproduction

```jsx
import { Month } from '@mantine/dates';

function Demo() {
  return (
    <Month
      month={new Date(2024, 0, 15)} // January 2024
      hideOutsideDates={true}
      minDate={new Date(2024, 0, 1)}
    />
  );
}
```

When navigating with the Tab key, the focus behavior is incorrect - it seems to be filtering dates based on the `minDate` month instead of the actual `month` prop that's being displayed.

### Expected behavior

The tab order should only include dates that are:
1. Within the displayed month when `hideOutsideDates` is true
2. Not disabled or excluded
3. After the minDate if specified

The keyboard navigation should work correctly and focus only on dates that belong to the currently displayed month.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
