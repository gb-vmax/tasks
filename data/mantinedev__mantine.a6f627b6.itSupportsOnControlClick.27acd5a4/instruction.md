# Bug Report

### Describe the bug

The `__onControlClick` callback is not being triggered when clicking on date picker control buttons. The callback should fire when clicking individual date/month/year buttons in the calendar, but nothing happens.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function Demo() {
  const handleControlClick = (value) => {
    console.log('Control clicked:', value);
  };

  return (
    <DatePicker
      __onControlClick={handleControlClick}
    />
  );
}
```

Steps to reproduce:
1. Set up a DatePicker with `__onControlClick` prop
2. Click on any date button in the calendar table
3. The callback is never invoked

### Expected behavior

The `__onControlClick` callback should be called with the date value (as a string) when clicking on individual control buttons inside the calendar table. The callback should receive the selected date/month/year value.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
