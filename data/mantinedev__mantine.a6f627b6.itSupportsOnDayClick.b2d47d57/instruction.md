# Bug Report

### Describe the bug

The `__onDayClick` callback is receiving incorrect arguments. When clicking on a day in the calendar component, the callback appears to be passing the event object instead of the date object as the second parameter.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function MyComponent() {
  const handleDayClick = (event, date) => {
    console.log('Date clicked:', date);
    // Expected: Date object
    // Actual: Event object is being passed instead
  };

  return (
    <DatePicker
      __onDayClick={handleDayClick}
    />
  );
}
```

When clicking on a day, the second parameter (`date`) contains the event object rather than the actual date that was clicked.

### Expected behavior

The `__onDayClick` callback should receive:
1. First parameter: the click event
2. Second parameter: the date object representing the clicked day

Currently it seems like both parameters are receiving the event object.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
