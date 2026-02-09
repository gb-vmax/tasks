# Bug Report

### Describe the bug

Keyboard navigation in the calendar month view is not working correctly. When using arrow keys to navigate between days, the focus jumps to the wrong day cell.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function Demo() {
  return <DatePicker />;
}
```

Steps to reproduce:
1. Open a calendar month view
2. Focus on a day cell (e.g., the 5th day)
3. Press the ArrowDown key
4. The focus moves to the wrong day - it skips a day instead of moving exactly one week down

Same issue happens with ArrowRight navigation - pressing right arrow from day 6 doesn't move to day 7 as expected.

### Expected behavior

- Pressing ArrowDown should move focus exactly 7 days forward (one week down)
- Pressing ArrowRight should move focus to the next day
- The navigation should be consistent and predictable

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
