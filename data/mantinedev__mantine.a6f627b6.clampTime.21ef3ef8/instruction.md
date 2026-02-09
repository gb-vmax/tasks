# Bug Report

### Describe the bug

The `TimePicker` component is not respecting the `max` time constraint properly. When I set a maximum time, values that should be allowed are being clamped incorrectly, and the component seems to default to the minimum value instead of properly handling the maximum boundary.

### Reproduction

```jsx
import { TimePicker } from '@mantine/dates';

function Demo() {
  return (
    <TimePicker
      defaultValue="15:00"
      min="09:00"
      max="18:00"
    />
  );
}
```

When trying to set a time like "15:00" (which is between min and max), the component clamps it to "09:00" instead of keeping it at "15:00".

Also, if I don't provide a `max` prop at all, times are being incorrectly clamped to very low values instead of allowing any time up to 23:59.

### Expected behavior

- Times within the min/max range should remain unchanged
- Times above max should be clamped to max
- Times below min should be clamped to min  
- When no max is provided, times should not be artificially limited

### System Info

- @mantine/dates version: latest
- @mantine/core version: 7.x
- React version: 18.x

---
Repository: /testbed
