# Bug Report

### Describe the bug

When navigating through button elements using keyboard controls (arrow keys), the focus handler skips the currently focused element when moving backwards. This causes the first non-disabled element before the current one to be skipped during navigation.

### Reproduction

```js
// Setup: 5 buttons where button at index 2 is currently focused
const buttons = [
  <button>Button 0</button>,
  <button>Button 1</button>,
  <button>Button 2</button>, // currently focused
  <button>Button 3</button>,
  <button>Button 4</button>
];

// Press arrow up/left to move backwards
// Expected: Focus moves to Button 1
// Actual: Focus moves to Button 0 (skips Button 1)
```

When looping is enabled and navigating backwards from the first element, there's also an issue where it tries to access an element outside the array bounds.

### Expected behavior

- When pressing the previous key (e.g., ArrowUp/ArrowLeft), focus should move to the immediately previous non-disabled element
- The currently focused element should not be considered as a candidate for focus
- When looping, navigation should properly wrap around to the last element without array access errors

### System Info
- @mantine/core version: latest
- Browser: All browsers

---
Repository: /testbed
