# Bug Report

### Describe the bug

The TimePicker component is displaying swapped values for hours and minutes. When I set a time like "14:30", it shows up as "30:14" instead. The hours and minutes are reversed in the initial display.

Also noticed that the clear button behavior is inverted - it only shows up when all fields are empty, but disappears when there's actually a time value to clear.

### Reproduction

```jsx
import { TimePicker } from '@mantine/dates';

function Demo() {
  return (
    <TimePicker 
      defaultValue={new Date('2024-01-01 14:30:00')}
      clearable
    />
  );
}
```

### Expected behavior

1. The time picker should display "14:30" (hours:minutes in correct order)
2. The clear button should be visible when there's a value to clear, not when the fields are empty

### System Info

- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
