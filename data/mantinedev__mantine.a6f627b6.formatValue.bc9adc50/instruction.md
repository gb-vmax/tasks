# Bug Report

### Describe the bug

I'm experiencing an issue with the `HiddenDatesInput` component when using date ranges. When only the start date is selected (without an end date), the component displays the wrong date value. It seems like the start and end dates are being swapped in the display logic.

### Reproduction

```jsx
import { HiddenDatesInput } from '@mantine/dates';

// Set up a date range with only start date
const startDate = new Date('2024-01-15');
const value = [startDate, null];

// The component shows nothing instead of showing "2024-01-15 –"
<HiddenDatesInput value={value} type="range" />
```

When I select a start date but haven't selected an end date yet, the input appears empty. If I have an end date but no start date, it displays incorrectly with the end date followed by " –".

### Expected behavior

- When only the start date is set: should display `"2024-01-15 –"` (start date with dash)
- When only the end date is set: should display nothing or handle appropriately
- When both dates are set: should display `"2024-01-15 – 2024-01-20"`

The current behavior seems backwards - it's checking for end date first when it should check for start date first in a date range scenario.

### System Info

- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
