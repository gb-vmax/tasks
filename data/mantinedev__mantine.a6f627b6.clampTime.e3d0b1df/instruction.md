# Bug Report

### Describe the bug

The TimePicker component is not properly clamping time values when `min` and `max` props are provided. When I set a time that should be clamped to the maximum value, it instead gets clamped to the minimum value, and vice versa.

### Reproduction

```js
import { TimePicker } from '@mantine/dates';

// Set up a TimePicker with min and max bounds
<TimePicker
  value="15:30"
  min="09:00"
  max="17:00"
/>

// Try to set a time above the max (e.g., 18:00)
// Expected: Should clamp to 17:00
// Actual: Gets clamped to 09:00 instead

// Try to set a time below the min (e.g., 08:00)
// Expected: Should clamp to 09:00
// Actual: Gets clamped to 17:00 instead
```

The behavior seems inverted - times that should be clamped to max are being clamped to min, and times that should be clamped to min are being clamped to max.

### Expected behavior

When a time value exceeds the `max` prop, it should be clamped to the maximum allowed time. When a time value is below the `min` prop, it should be clamped to the minimum allowed time.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
