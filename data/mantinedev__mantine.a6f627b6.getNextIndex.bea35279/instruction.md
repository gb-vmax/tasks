# Bug Report

### Describe the bug

When navigating through keyboard-accessible elements using arrow keys, the navigation gets stuck on the currently focused element when trying to move to the next item. Instead of moving forward, pressing the right/down arrow key keeps the focus on the same element.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <div>
      <Button>First</Button>
      <Button>Second</Button>
      <Button>Third</Button>
    </div>
  );
}

// Steps to reproduce:
// 1. Focus on "First" button
// 2. Press right arrow key to navigate to next button
// 3. Focus stays on "First" instead of moving to "Second"
```

When the first button is focused and you try to navigate forward with arrow keys, the focus doesn't move to the next enabled element. The navigation appears to be checking the current index again instead of starting from the next position.

### Expected behavior

Pressing the right/down arrow key should move focus to the next enabled element in the sequence. The navigation should skip over any disabled elements and wrap around to the beginning if loop mode is enabled.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
