# Bug Report

### Describe the bug

The `__onDayClick` callback is receiving incorrect data when clicking on day cells in date picker components. Instead of receiving the date value, it appears to be receiving the click event object.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function MyComponent() {
  const handleDayClick = (event, date) => {
    console.log('Date received:', date);
    // Expected: Date string or Date object
    // Actual: Click event object
  };

  return (
    <DatePicker
      __onDayClick={handleDayClick}
    />
  );
}
```

When clicking on any day in the calendar:
1. The callback fires correctly
2. But the `date` parameter contains the event object instead of the actual date
3. This makes it impossible to get the selected date value from the callback

### Expected behavior

The `__onDayClick` callback should receive the date value as its second parameter, not the event object. The first parameter should be the event, and the second should be the date that was clicked.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
