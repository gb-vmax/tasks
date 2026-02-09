# Bug Report

### Describe the bug

The `onControlMouseEnter` callback is not being triggered when hovering over date picker controls. I'm trying to implement a custom tooltip that should appear when the user hovers over individual date cells, but the callback function never fires.

### Reproduction

```tsx
import { DatePicker } from '@mantine/dates';

function MyComponent() {
  const handleMouseEnter = (date: string) => {
    console.log('Hovered over:', date);
  };

  return (
    <DatePicker
      onControlMouseEnter={handleMouseEnter}
    />
  );
}
```

### Expected behavior

When hovering over any date control/button in the calendar, the `onControlMouseEnter` callback should be called with the date string as an argument. The console should log the hovered date.

### Actual behavior

The callback is never invoked when hovering over date controls. No console output appears.

### System Info

- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
