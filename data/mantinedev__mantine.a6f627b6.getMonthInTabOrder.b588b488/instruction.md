# Bug Report

### Describe the bug

I'm experiencing an issue with the MonthsList component where keyboard navigation is completely broken. When trying to tab through the month picker, it seems like the focus is going to disabled months instead of enabled ones, and when there's no specific month to focus on, it's focusing on the last month instead of the first one.

### Reproduction

```tsx
import { MonthsList } from '@mantine/dates';

// Set up a month picker with some disabled months
<MonthsList
  minDate={new Date(2024, 3, 1)} // April
  maxDate={new Date(2024, 8, 30)} // September
/>
```

When I try to tab into the month picker:
- The focus goes to disabled months (months outside the min/max range) instead of skipping them
- If I don't have a selected month or current month in range, it focuses on the last enabled month instead of the first one

### Expected behavior

The month picker should:
1. Only allow tabbing to enabled (non-disabled) months
2. Default to focusing the first enabled month when there's no selected/current month in the valid range

This makes the component really hard to use with keyboard navigation. It seems like the logic for determining which month should receive focus is inverted somehow.

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox (happens in both)

---
Repository: /testbed
