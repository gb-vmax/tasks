# Bug Report

### Describe the bug

Keyboard navigation in the date picker is broken. When trying to navigate between dates using arrow keys, the focus jumps to incorrect cells or gets stuck and doesn't move at all.

### Reproduction

```js
import { DatePicker } from '@mantine/dates';

function Demo() {
  return <DatePicker />;
}

// Steps to reproduce:
// 1. Open the date picker calendar
// 2. Focus on any date cell
// 3. Try to navigate using arrow keys (up/down/left/right)
// 4. The focus either doesn't move or jumps to the wrong date
```

### Expected behavior

Arrow key navigation should move focus to adjacent date cells in the expected direction:
- Right arrow → next day
- Left arrow → previous day  
- Down arrow → same day next week
- Up arrow → same day previous week

### System Info

- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
