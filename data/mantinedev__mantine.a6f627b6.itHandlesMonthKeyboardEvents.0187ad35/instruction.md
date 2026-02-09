# Bug Report

### Describe the bug

Arrow key navigation in the month calendar is off by one day. When pressing ArrowDown, the focus moves to the wrong day in the next week.

### Reproduction

```jsx
// Create a month calendar component
const calendar = render(<MonthCalendar />);
const days = calendar.getAllByRole('button');

// Focus on day 5 (index 4)
days[4].focus();

// Press ArrowDown to move to next week
// Expected: Focus should move to day 12 (index 11)
// Actual: Focus moves to day 11 (index 10)
```

The same issue occurs when:
- Navigating across multiple months with arrow keys
- Using ArrowDown from the last row of the calendar

### Expected behavior

When pressing ArrowDown, the focus should move exactly 7 days forward (one week down in the calendar grid). Currently it seems to be moving to an incorrect position.

### System Info
- Mantine version: latest
- React version: 18.x

---
Repository: /testbed
