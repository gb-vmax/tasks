# Bug Report

### Describe the bug

When using the `TimeValue` component with a Date object, the displayed time shows incorrect values. Instead of showing the hours, it appears to be displaying the day of the month, and the seconds field (when enabled) shows minutes instead of seconds.

### Reproduction

```js
import { TimeValue } from '@mantine/dates';

const date = new Date('2024-01-15T14:30:45'); // 2:30:45 PM on Jan 15th

// Expected: "14:30:45"
// Actual: "15:30:30" (shows day=15, minutes=30, minutes=30)
<TimeValue value={date} withSeconds />
```

### Expected behavior

The component should display the time in HH:MM:SS format (or HH:MM without seconds), showing the actual hours, minutes, and seconds from the Date object.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
