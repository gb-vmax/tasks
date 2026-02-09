# Bug Report

### Describe the bug

Keyboard navigation is skipping elements when using arrow keys to navigate through a list of items. When pressing the down/right arrow key, it appears to skip the next immediate item and jump to the one after it instead.

### Reproduction

```jsx
const items = [
  { id: 1, label: 'Item 1', disabled: false },
  { id: 2, label: 'Item 2', disabled: false },
  { id: 3, label: 'Item 3', disabled: false },
  { id: 4, label: 'Item 4', disabled: false },
];

// When focused on Item 1 and pressing arrow down/right:
// Expected: Focus moves to Item 2
// Actual: Focus jumps to Item 3, skipping Item 2
```

Steps to reproduce:
1. Create a component with multiple focusable elements
2. Focus on the first element
3. Press the down arrow or right arrow key
4. Notice that it skips the immediate next element

Also, when looping is enabled and you're on the last element, pressing the arrow key doesn't properly wrap around to the first element - it seems to get stuck or behave unexpectedly.

### Expected behavior

Arrow key navigation should move focus to the immediate next enabled element, not skip over it. When looping is enabled and at the last element, it should wrap to the first element.

### System Info
- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
