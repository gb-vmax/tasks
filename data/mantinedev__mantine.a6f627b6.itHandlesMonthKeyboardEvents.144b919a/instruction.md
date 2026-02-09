# Bug Report

### Describe the bug

Arrow key navigation in the date picker is not working correctly. When pressing the down arrow key, the focus moves to the wrong day - it's off by one day.

### Reproduction

1. Open a month view in the date picker
2. Focus on a day (e.g., day 4)
3. Press the down arrow key
4. Expected: Focus should move to day 11 (one week down)
5. Actual: Focus moves to day 10 instead

The same issue occurs when navigating between months:
1. Focus on the first day of the second month
2. Press down arrow
3. Expected: Focus should move to day 7 (one week down) 
4. Actual: Focus moves to day 6

### Expected behavior

Pressing the down arrow key should move focus exactly one week down (7 days) in the calendar grid. The focus should land on the correct day that is 7 positions below the current focused day.

### System Info
- @mantine/dates version: latest
- Browser: Any

---
Repository: /testbed
