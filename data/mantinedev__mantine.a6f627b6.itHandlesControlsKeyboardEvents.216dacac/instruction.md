# Bug Report

### Describe the bug

Keyboard navigation in date picker controls is not working as expected. When using arrow keys to navigate between date controls, the focus moves to incorrect elements or doesn't move at all.

### Reproduction

```jsx
// Create a date picker with multiple controls
const { container } = render(<DatePicker />);
const controls = container.querySelectorAll('[data-mantine-control]');

// Try navigating with arrow keys
// 1. Focus on second control (index 1)
// 2. Press ArrowDown
// Expected: Focus moves to control at index 4
// Actual: Focus stays on current control or moves to wrong element

// Similarly with ArrowUp:
// 1. Focus on control at index 3
// 2. Press ArrowUp
// Expected: Focus moves to control at index 0
// Actual: Focus doesn't move
```

### Expected behavior

- **ArrowDown** should move focus down by the number of columns (e.g., from index 1 to index 4 in a grid)
- **ArrowUp** should move focus up by the number of columns (e.g., from index 3 to index 0)
- **ArrowRight** should move focus to the next column when at the end of a column
- **ArrowLeft** should move focus to the previous column when at the start of a column

### Additional context

This affects multi-column date picker layouts (e.g., `numberOfColumns=2`). The keyboard navigation seems to be broken in both single and multi-column configurations. Users expect standard grid keyboard navigation patterns to work correctly.

---
Repository: /testbed
