# Bug Report

### Describe the bug

The weekday ordering in date components is incorrect. When no `firstDayOfWeek` prop is specified, the week is starting on Tuesday instead of Monday. Additionally, when setting `firstDayOfWeek={0}` (which should start the week on Sunday), the week is still starting on Monday.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';

// Default behavior - should start with Monday but starts with Tuesday
<Calendar />
// Weekdays render as: Tu, We, Th, Fr, Sa, Su, Mo

// Setting firstDayOfWeek to 0 (Sunday) - should start with Sunday but starts with Monday
<Calendar firstDayOfWeek={0} />
// Weekdays render as: Mo, Tu, We, Th, Fr, Sa, Su
```

### Expected behavior

- By default (no `firstDayOfWeek` prop), the week should start on Monday: `Mo, Tu, We, Th, Fr, Sa, Su`
- When `firstDayOfWeek={0}`, the week should start on Sunday: `Su, Mo, Tu, We, Th, Fr, Sa`
- When `firstDayOfWeek={6}`, the week should start on Saturday: `Sa, Su, Mo, Tu, We, Th, Fr`

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
