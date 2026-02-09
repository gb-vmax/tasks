# Bug Report

### Describe the bug

The `__onDayClick` callback is receiving a string instead of a Date object when a day is clicked in the calendar component. According to the API, the callback should receive a Date object, but it's currently passing a string representation of the date.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function MyComponent() {
  const handleDayClick = (date) => {
    console.log(typeof date); // Expected: "object", Actual: "string"
    console.log(date instanceof Date); // Expected: true, Actual: false
  };

  return <DatePicker __onDayClick={handleDayClick} />;
}
```

When clicking on any day in the calendar, the `__onDayClick` callback receives a string instead of a Date object. This makes it difficult to work with the date value directly without additional parsing.

### Expected behavior

The `__onDayClick` callback should receive a Date object, not a string. This would be consistent with other date-related callbacks in the library and allow for direct date manipulation without needing to convert from string first.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
