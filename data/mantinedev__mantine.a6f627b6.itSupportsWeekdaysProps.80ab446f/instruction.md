# Bug Report

### Describe the bug

The `firstDayOfWeek` setting doesn't appear to be working correctly. When using `firstDayOfWeek` with a custom `weekdayFormat` function, the weekdays are displayed in the wrong order.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';
import { DatesProvider } from '@mantine/dates';
import dayjs from 'dayjs';

// Using weekdayFormat with default firstDayOfWeek
<Calendar
  weekdayFormat={(date) => dayjs(date).format('dd')[0]}
/>
// Expected: ['M', 'T', 'W', 'T', 'F', 'S', 'S']
// Actual: ['T', 'W', 'T', 'F', 'S', 'S', 'M']

// Using DatesProvider with firstDayOfWeek
<DatesProvider settings={{ firstDayOfWeek: 4 }}>
  <Calendar />
</DatesProvider>
// The week starts on the wrong day
```

### Expected behavior

When `weekdayFormat` is provided, the weekdays should start with Monday ('M') by default. When `firstDayOfWeek` is set to 4 (Thursday), the week should start on Thursday.

### System Info

- @mantine/dates: latest
- @mantine/core: latest

---
Repository: /testbed
