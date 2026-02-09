# Bug Report

### Describe the bug

The `onControlMouseEnter` callback is not being triggered when hovering over date picker control buttons. It seems like the hover event isn't properly propagating from the button elements to trigger the callback.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function Demo() {
  const handleMouseEnter = (date) => {
    console.log('Hovered date:', date);
  };

  return (
    <DatePicker
      onControlMouseEnter={handleMouseEnter}
    />
  );
}
```

When hovering over individual date buttons in the calendar, the `onControlMouseEnter` callback doesn't fire. Expected the callback to be called with the date value when hovering over any calendar control button.

### Expected behavior

The `onControlMouseEnter` callback should be triggered when hovering over date picker buttons, and it should receive the corresponding date as an argument.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
