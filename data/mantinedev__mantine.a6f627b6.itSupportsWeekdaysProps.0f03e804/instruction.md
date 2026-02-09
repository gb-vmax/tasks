# Bug Report

### Describe the bug

The `firstDayOfWeek` prop seems to be off by one day. When setting `firstDayOfWeek={0}`, the week starts with Monday instead of Sunday. According to standard conventions, 0 should represent Sunday as the first day of the week.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';

// Expected: Week should start with Sunday
// Actual: Week starts with Monday
<Calendar firstDayOfWeek={0} />
```

When I set `firstDayOfWeek={0}`, I see the weekdays displayed as:
Mo, Tu, We, Th, Fr, Sa, Su

But I expected:
Su, Mo, Tu, We, Th, Fr, Sa

### Expected behavior

- `firstDayOfWeek={0}` should display Sunday as the first day
- `firstDayOfWeek={1}` should display Monday as the first day
- And so on...

This follows the standard convention where 0 = Sunday, 1 = Monday, etc.

The same issue occurs when using `DatesProvider` to set the first day of week globally.

---
Repository: /testbed
