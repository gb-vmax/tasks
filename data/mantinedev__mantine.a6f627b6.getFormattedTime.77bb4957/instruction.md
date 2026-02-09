# Bug Report

### Describe the bug

When displaying time in 12-hour format, the TimeValue component is showing incorrect hour values and AM/PM indicators. Specifically, times at 12:00 PM (noon) are being displayed as 0:00 PM, and 12:00 AM (midnight) is showing as 12:00 PM instead of 12:00 AM.

### Reproduction

```jsx
import { TimeValue } from '@mantine/dates';

// This should display "12:00 PM" but shows "0:00 PM"
<TimeValue value="12:00" format="12" />

// This should display "12:00 AM" but shows "12:00 PM"
<TimeValue value="00:00" format="12" />
```

### Expected behavior

- 12:00 (noon) should be displayed as "12:00 PM"
- 00:00 (midnight) should be displayed as "12:00 AM"
- Hours should never show as "0" in 12-hour format

In 12-hour time format:
- 00:00 - 00:59 should display as 12:00 AM - 12:59 AM
- 12:00 - 12:59 should display as 12:00 PM - 12:59 PM
- 13:00 - 23:59 should display as 1:00 PM - 11:59 PM

### System Info

- @mantine/dates version: latest
- Browser: All browsers

---
Repository: /testbed
