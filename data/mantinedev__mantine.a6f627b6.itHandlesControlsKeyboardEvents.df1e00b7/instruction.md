# Bug Report

### Describe the bug

Keyboard navigation in date picker controls is not working as expected. When using arrow keys to navigate between date cells, the focus moves to the wrong cell.

### Reproduction

```jsx
// Create a date picker component with keyboard navigation
const picker = render(<DatePicker />);
const controls = getAllControls();

// Start at position [0, 1] (second cell in first row)
controls[1].focus();

// Press ArrowDown - should move to cell directly below
// Expected: focus moves to controls[4] (same column, next row)
// Actual: focus moves to controls[3] (wrong cell)
```

Similar issue occurs when navigating between columns:

```jsx
// Navigate to last cell in first column
firstColumnControls[lastIndex].focus();

// Press ArrowRight - should move to first cell of next column
// Expected: focus moves to secondColumnControls[0]
// Actual: focus moves to secondColumnControls[1] (skips first cell)
```

### Expected behavior

Arrow key navigation should move focus to the correct adjacent cell:
- ArrowDown should move to the cell directly below in the same column
- ArrowRight should move to the first cell of the next column when at the end of current column

### System Info
- Mantine version: latest
- Browser: tested on Chrome and Firefox

---
Repository: /testbed
