# Bug Report

### Describe the bug

Arrow key navigation in date picker controls is not working correctly. When pressing ArrowDown from the second control, focus moves to the wrong element. Similarly, ArrowLeft navigation from the second column doesn't behave as expected.

### Reproduction

```js
// Start with focus on the second control (index 1)
// Press ArrowDown
// Expected: Focus should move to control at index 4 (one row down)
// Actual: Focus moves to control at index 3 (incorrect position)

// When navigating between columns:
// Start with focus on first control of second column (index 0)
// Press ArrowLeft
// Expected: Should move to last control of first column
// Actual: Navigation doesn't work from this position
```

### Expected behavior

- ArrowDown should move focus down by one full row (typically 3 positions in a calendar grid)
- ArrowLeft from the first control of the second column should wrap to the last control of the first column

### System Info
- Mantine version: latest
- Browser: All browsers affected

---
Repository: /testbed
