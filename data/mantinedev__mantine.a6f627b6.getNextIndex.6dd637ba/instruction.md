# Bug Report

### Describe the bug

I'm experiencing an issue with keyboard navigation in the date picker component. When navigating between different calendar levels (month/year/decade views) and rows using arrow keys, the focus sometimes jumps to incorrect cells or skips cells entirely.

### Reproduction

```js
import { DatePicker } from '@mantine/dates';

function Demo() {
  return <DatePicker />;
}

// Steps to reproduce:
// 1. Open the date picker
// 2. Click on the month/year header to go to month selection view
// 3. Use the Up arrow key to navigate between rows
// 4. Notice that focus jumps to the wrong cell (off by one position)
// 5. Try navigating from the last cell of a row upward
// 6. The focus lands on an incorrect cell in the previous row
```

### Expected behavior

When using arrow keys to navigate:
- Up arrow should move focus to the cell directly above in the previous row
- When moving up from the bottom row to upper levels, focus should land on the correct corresponding cell
- Navigation should feel natural and predictable, with focus landing on the visually aligned cell

### System Info

- @mantine/dates version: latest
- Browser: Chrome/Firefox
- OS: macOS

The navigation feels off by one position in certain scenarios, particularly when moving between calendar levels or when at row boundaries.

---
Repository: /testbed
