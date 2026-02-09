# Bug Report

### Describe the bug

Arrow key navigation is not working correctly in RTL (right-to-left) mode. When using keyboard navigation with arrow keys, pressing the right arrow moves to the previous item and pressing the left arrow moves to the next item, which is the opposite of the expected behavior in RTL layouts.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function RTLNavigation() {
  return (
    <Box dir="rtl">
      <button>Item 1</button>
      <button>Item 2</button>
      <button>Item 3</button>
    </Box>
  );
}

// Steps:
// 1. Set direction to 'rtl'
// 2. Focus on Item 2
// 3. Press ArrowRight key
// Expected: Focus moves to Item 1 (previous in RTL)
// Actual: Focus moves to Item 3 (next item)
```

### Expected behavior

In RTL mode:
- ArrowRight should move to the previous item (moving right visually)
- ArrowLeft should move to the next item (moving left visually)

Currently it seems like the arrow key directions are not being inverted for RTL layouts, so the navigation feels backwards.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
