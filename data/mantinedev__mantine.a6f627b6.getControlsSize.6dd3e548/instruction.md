# Bug Report

### Describe the bug

Keyboard navigation in date picker components is broken after a recent update. When trying to navigate between dates using arrow keys, the navigation behaves incorrectly or doesn't work at all.

### Reproduction

```js
import { DatePicker } from '@mantine/dates';

function Demo() {
  return <DatePicker />;
}

// Steps:
// 1. Open the date picker
// 2. Try to navigate using arrow keys (up/down/left/right)
// 3. Navigation doesn't work as expected - cursor movement is incorrect
```

### Expected behavior

Arrow keys should properly navigate through the calendar grid:
- Right arrow: move to next day
- Left arrow: move to previous day  
- Down arrow: move to next week
- Up arrow: move to previous week

The keyboard controls were working fine before but now seem to be calculating the grid dimensions incorrectly.

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
