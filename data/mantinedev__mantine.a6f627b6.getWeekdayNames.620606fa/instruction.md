# Bug Report

### Describe the bug

The weekdays row in the calendar component is only showing 6 days instead of 7. The last day of the week is missing from the display.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';

function Demo() {
  return <Calendar />;
}
```

When rendering a calendar component, the weekday header row only displays 6 weekday names (e.g., Mon, Tue, Wed, Thu, Fri, Sat) and the 7th day (Sunday or Monday depending on `firstDayOfWeek` setting) is missing.

This also happens when using custom format strings or format functions:

```jsx
<Calendar
  weekdayFormat={(date) => dayjs(date).format('ddd')}
/>
```

### Expected behavior

The weekdays row should display all 7 days of the week, not just 6. For example, with default settings it should show: Mon, Tue, Wed, Thu, Fri, Sat, Sun.

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
