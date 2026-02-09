# Bug Report

### Describe the bug

Keyboard navigation in the month picker component is not working correctly. When using arrow keys to navigate between dates, the focus moves to the wrong day cell.

### Reproduction

```jsx
// Create a month picker component
const picker = <MonthPicker defaultDate={new Date(2024, 0, 1)} />

// Focus on a day cell (e.g., 5th day)
// Press ArrowDown key
// Expected: Focus should move down one week (7 days forward) to day 12
// Actual: Focus moves to day 11 instead
```

Similar issue occurs when navigating upward:
```jsx
// Focus on day 15 in the second month view
// Press ArrowUp key  
// Expected: Focus should move up one week (7 days backward) to day 8
// Actual: Focus moves to day 7 instead
```

### Expected behavior

Arrow key navigation should move focus by exactly 7 days when pressing ArrowUp/ArrowDown:
- ArrowDown: Move focus 7 days forward (one week down)
- ArrowUp: Move focus 7 days backward (one week up)

The calculation seems to be off by one day in both directions.

### System Info
- Mantine version: latest
- React version: 18.x
- Browser: All browsers affected

---
Repository: /testbed
