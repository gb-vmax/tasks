# Bug Report

### Describe the bug
Keyboard navigation is skipping elements when using arrow keys to navigate through a list of buttons. When pressing the up/left arrow keys, the focus jumps over elements instead of moving to the immediately previous enabled button.

### Reproduction
```js
// Create a list of buttons with keyboard navigation
const buttons = [
  { label: 'Button 1', disabled: false },
  { label: 'Button 2', disabled: false },
  { label: 'Button 3', disabled: false },
  { label: 'Button 4', disabled: false },
]

// Focus on Button 4 and press up arrow
// Expected: Focus moves to Button 3
// Actual: Focus moves to Button 2 (skips Button 3)
```

### Expected behavior
When navigating backwards with arrow keys, focus should move to the immediately previous non-disabled button, not skip over buttons.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
