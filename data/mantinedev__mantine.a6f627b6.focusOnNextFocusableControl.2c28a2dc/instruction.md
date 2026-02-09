# Bug Report

### Describe the bug

Keyboard navigation in the date picker calendar is completely broken. When trying to navigate between dates using arrow keys, the focus doesn't move at all and stays on the current cell. This makes the calendar unusable for keyboard-only users.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function Demo() {
  return <DatePicker />;
}
```

Steps to reproduce:
1. Open the date picker calendar
2. Focus on any date cell
3. Press arrow keys (up, down, left, right) to navigate
4. The focus remains on the same cell instead of moving to adjacent dates

### Expected behavior

Arrow keys should move focus between date cells in the calendar:
- Right arrow: move to next day
- Left arrow: move to previous day  
- Down arrow: move to next week
- Up arrow: move to previous week

The focus should traverse through the calendar grid and wrap to the next/previous month when reaching boundaries.

### System Info
- @mantine/dates version: latest
- Browser: All browsers

---
Repository: /testbed
