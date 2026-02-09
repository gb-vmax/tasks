# Bug Report

### Describe the bug

Keyboard navigation in the date picker is broken. When using arrow keys to navigate between dates, the focus doesn't move at all and the keyboard controls are completely unresponsive.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function Demo() {
  return <DatePicker />;
}
```

Steps to reproduce:
1. Open the date picker calendar
2. Try to use arrow keys (up, down, left, right) to navigate between dates
3. Nothing happens - the focus stays on the same date

### Expected behavior

Arrow keys should move focus between dates in the calendar. For example:
- Right arrow should move to the next day
- Left arrow should move to the previous day
- Down arrow should move to the same day in the next week
- Up arrow should move to the same day in the previous week

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
