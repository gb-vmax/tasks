# Bug Report

### Describe the bug

Keyboard navigation in date picker controls is broken. When using arrow keys to navigate through calendar dates, the focus jumps to incorrect positions or gets stuck, making it impossible to navigate properly through the calendar grid.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function Demo() {
  return <DatePicker />;
}

// Steps to reproduce:
// 1. Open the date picker
// 2. Use arrow keys (up/down/left/right) to navigate between dates
// 3. Notice that the focus moves to wrong cells or doesn't move at all
```

The navigation seems to calculate the grid size incorrectly, causing the focus to jump to unexpected positions instead of moving to adjacent dates.

### Expected behavior

Arrow keys should move focus to the adjacent date cells in the calendar grid:
- Right arrow: move to next day
- Left arrow: move to previous day  
- Down arrow: move to same day next week
- Up arrow: move to same day previous week

### System Info

- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
