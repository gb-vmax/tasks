# Bug Report

### Describe the bug

The `onControlMouseEnter` callback is not being triggered when hovering over date picker controls. I expected the callback to fire with the date information when I move my mouse over a date cell, but nothing happens.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function MyComponent() {
  const handleMouseEnter = (date) => {
    console.log('Mouse entered:', date);
  };

  return (
    <DatePicker
      onControlMouseEnter={handleMouseEnter}
    />
  );
}
```

Steps to reproduce:
1. Create a DatePicker component with `onControlMouseEnter` prop
2. Hover over any date cell in the calendar
3. The callback doesn't get called

### Expected behavior

The `onControlMouseEnter` callback should be triggered when hovering over date controls, and it should receive the date value as a string parameter.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
