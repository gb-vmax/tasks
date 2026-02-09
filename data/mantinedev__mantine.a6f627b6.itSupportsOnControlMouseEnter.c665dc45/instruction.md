# Bug Report

### Describe the bug

The `onControlMouseEnter` callback is not being triggered when hovering over date picker control buttons. I'm trying to implement a custom tooltip/preview feature that should activate when the user hovers over individual date cells, but the callback doesn't seem to fire.

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

When hovering over the date buttons in the calendar table, the `handleMouseEnter` function is never called. Expected it to receive the date value as a parameter when hovering over each date cell.

### Expected behavior

The `onControlMouseEnter` callback should be triggered when hovering over individual date control buttons in the calendar, and it should receive the corresponding date information.

### System Info
- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
