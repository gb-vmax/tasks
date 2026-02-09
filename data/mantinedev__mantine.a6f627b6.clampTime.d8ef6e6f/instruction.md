# Bug Report

### Describe the bug

The `TimePicker` component is not respecting the `min` and `max` time constraints properly. When I try to set a time value that should be clamped within the specified range, it seems to be doing the opposite - values that should be valid are being rejected, and values outside the range are being accepted.

### Reproduction

```jsx
import { TimePicker } from '@mantine/dates';

// Set up a TimePicker with min and max constraints
<TimePicker
  value="14:00"
  min="09:00"
  max="17:00"
/>
```

When trying to programmatically set or validate times:
- Times between 09:00 and 17:00 are being clamped incorrectly
- Times outside this range are not being properly constrained
- The behavior is inverted from what's expected

### Expected behavior

The TimePicker should:
- Accept and maintain times between the min (09:00) and max (17:00) values
- Clamp times below 09:00 to 09:00
- Clamp times above 17:00 to 17:00

Instead, it appears to be doing the reverse of this logic.

### System Info

- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
