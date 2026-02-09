# Bug Report

### Describe the bug

The TimePicker component is not correctly formatting time strings based on the `format` prop. When using 12-hour format (AM/PM), the time is being displayed in 24-hour format instead, and vice versa.

### Reproduction

```tsx
import { TimePicker } from '@mantine/dates';

// Example 1: 12-hour format
<TimePicker format="12" value={new Date('2024-01-01 14:30:00')} />
// Expected: "02:30 PM"
// Actual: "14:30"

// Example 2: 24-hour format  
<TimePicker format="24" value={new Date('2024-01-01 14:30:00')} />
// Expected: "14:30"
// Actual: "02:30 PM"
```

The formats appear to be inverted - when I specify 12-hour format, I get 24-hour output, and when I specify 24-hour format, I get 12-hour output with AM/PM.

### Expected behavior

- When `format="12"` is set, times should be displayed in 12-hour format with AM/PM indicators
- When `format="24"` is set, times should be displayed in 24-hour format without AM/PM

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
