# Bug Report

### Describe the bug

When using the TimePicker component with seconds enabled, the seconds field is being initialized with the minutes value instead of the actual seconds value from the time. This causes the seconds to display incorrectly when a time value is provided.

### Reproduction

```jsx
import { TimePicker } from '@mantine/dates';

function Demo() {
  return (
    <TimePicker 
      value="10:30:45" 
      withSeconds 
    />
  );
}
```

When the component renders, the seconds field shows "30" (the minutes value) instead of "45" (the actual seconds value).

### Expected behavior

The seconds field should display the correct seconds value from the provided time string. In the example above, it should show "45" not "30".

### System Info

- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
