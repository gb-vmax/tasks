# Bug Report

### Describe the bug

I'm experiencing an issue where clicking on date controls in the calendar doesn't trigger the `__onControlClick` callback. The callback should fire when clicking on individual date buttons, but it seems like nothing happens.

### Reproduction

```tsx
import { DatePicker } from '@mantine/dates';

function MyComponent() {
  const handleControlClick = (value: string) => {
    console.log('Control clicked:', value);
  };

  return (
    <DatePicker 
      __onControlClick={handleControlClick}
    />
  );
}
```

When clicking on any date button in the calendar, the `handleControlClick` function is not being called. I expected it to log the clicked date value to the console.

### Expected behavior

The `__onControlClick` callback should be triggered when clicking on individual date control buttons in the calendar table, and it should receive the date value as a string parameter.

### System Info
- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
