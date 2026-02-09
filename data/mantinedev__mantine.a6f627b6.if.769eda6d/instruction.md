# Bug Report

### Describe the bug

I'm experiencing an issue with the TimePicker component where trying to focus on the hours field causes unexpected behavior. When calling the focus function with `'hours'` as the parameter, it seems to trigger both focus and blur operations, or the focus doesn't work at all.

### Reproduction

```tsx
import { useTimePicker } from '@mantine/dates';

const MyComponent = () => {
  const timePicker = useTimePicker({ ... });
  
  // Try to focus the hours field
  timePicker.focus('hours');
  
  // Expected: hours input should be focused
  // Actual: focus behavior is broken
}
```

### Expected behavior

When calling `focus('hours')`, the hours input field should receive focus and allow the user to start typing immediately. The field should remain focused until the user moves to another field or clicks elsewhere.

### System Info
- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
