# Bug Report

### Describe the bug

The weekday names in the calendar are displaying incorrectly - they appear to be shifted by one day. For example, if the calendar should start with Sunday, it's showing Monday's label instead, and all subsequent days are shifted forward by one position.

### Reproduction

```jsx
import { WeekdaysRow } from '@mantine/dates';

// With firstDayOfWeek set to 0 (Sunday)
<WeekdaysRow 
  locale="en" 
  firstDayOfWeek={0}
  format="ddd"
/>

// Expected: Sun, Mon, Tue, Wed, Thu, Fri, Sat
// Actual: Mon, Tue, Wed, Thu, Fri, Sat, Sun
```

The same issue occurs regardless of which day is set as the first day of the week - the labels are always off by one day.

### Expected behavior

The weekday labels should correctly display starting from the specified `firstDayOfWeek` value. When `firstDayOfWeek={0}`, it should show Sunday as the first column, when `firstDayOfWeek={1}`, it should show Monday as the first column, etc.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
