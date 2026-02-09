# Bug Report

### Describe the bug

Keyboard navigation in the date picker calendar is not working correctly. When navigating with arrow keys, the focus jumps to the wrong day cells.

### Reproduction

1. Open a calendar/date picker component
2. Focus on a day in the middle of the month (e.g., day 5)
3. Press the down arrow key
4. Expected: Focus should move to day 12 (one week down)
5. Actual: Focus moves to day 11 instead

Also experiencing issues when navigating between multiple months:
1. Have a calendar showing two months side by side
2. Focus on a day in the second month (e.g., day 8)
3. Press the left arrow key
4. Expected: Focus should move to day 7 in the same month
5. Actual: Focus incorrectly jumps to day 7 in the first month

### Expected behavior

Arrow key navigation should move focus to the correct adjacent day cells:
- ArrowDown: Move down by 7 days (one week)
- ArrowUp: Move up by 7 days (one week)
- ArrowLeft: Move to previous day
- ArrowRight: Move to next day

Focus should stay within the current month unless navigating past the month boundaries.

### System Info
- Component: MonthPicker/Calendar
- Browser: Latest Chrome

---
Repository: /testbed
