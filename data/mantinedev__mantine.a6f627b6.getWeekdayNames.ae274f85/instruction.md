# Bug Report

### Describe the bug

The weekday names row is showing 8 days instead of 7 when rendered. Additionally, the first day of the week appears to be off by one day from what's expected.

### Reproduction

```jsx
import { WeekdaysRow } from '@mantine/dates';

// This renders 8 weekday labels instead of 7
<WeekdaysRow locale="en" firstDayOfWeek={1} />

// The first day shown is also incorrect - when setting firstDayOfWeek to 1 (Monday),
// it actually starts from Sunday instead
```

### Expected behavior

The weekdays row should:
1. Display exactly 7 days (one for each day of the week)
2. Start from the correct day when `firstDayOfWeek` is specified (e.g., Monday when `firstDayOfWeek={1}`)

Currently getting an extra day in the output and the starting day is shifted incorrectly.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
