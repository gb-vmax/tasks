# Bug Report

### Describe the bug

The keyboard navigation in the Month picker component is not working correctly. When using arrow keys to navigate between dates, the focus doesn't move to the expected day cell.

### Reproduction

```jsx
import { MonthPicker } from '@mantine/dates';

function Demo() {
  return <MonthPicker />;
}

// Steps to reproduce:
// 1. Open the month picker calendar
// 2. Focus on a day cell (e.g., the 5th day)
// 3. Press ArrowDown key
// Expected: Focus should move to the day in the next week (7 days forward)
// Actual: Focus moves to a different day than expected

// Another issue:
// 1. Focus on the 7th day of the month
// 2. Press ArrowRight key
// Expected: Focus should move to the 8th day
// Actual: Focus stays on the same day or moves incorrectly
```

### Expected behavior

- Pressing ArrowDown should move focus to the day cell 7 days forward (same weekday, next week)
- Pressing ArrowRight should move focus to the next day cell
- Keyboard navigation should follow a consistent grid pattern matching the visual calendar layout

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
