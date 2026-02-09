# Bug Report

### Describe the bug

The Month component is not displaying the last day of the month correctly. When rendering a calendar month, the final day is missing from the grid, causing the month view to be incomplete.

### Reproduction

```js
import { Month } from '@mantine/dates';

// Render a month component for any month
<Month month={new Date(2024, 0, 1)} /> // January 2024

// The last day of the month (January 31st) is not displayed in the calendar grid
// Only days 1-30 are shown
```

### Expected behavior

All days of the month should be displayed in the calendar grid, including the last day. For January 2024, days 1 through 31 should all be visible.

### System Info
- @mantine/dates version: latest
- Browser: All browsers affected

---
Repository: /testbed
