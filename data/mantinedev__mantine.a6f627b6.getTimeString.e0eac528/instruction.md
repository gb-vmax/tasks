# Bug Report

### Describe the bug
When using the TimePicker component with 24-hour format and `withSeconds` prop, the seconds are not being displayed in the time string. It seems like the logic is inverted - seconds are hidden when `withSeconds` is true and shown when it's false.

### Reproduction
```jsx
import { TimePicker } from '@mantine/dates';

// This should display seconds but doesn't
<TimePicker withSeconds format="24" />

// Meanwhile, when withSeconds is false, seconds appear (which shouldn't happen)
<TimePicker withSeconds={false} format="24" />
```

### Expected behavior
When `withSeconds={true}` is set with 24-hour format, the time string should include seconds in the format `HH:MM:SS`. When `withSeconds={false}` or not provided, it should only show `HH:MM`.

Currently experiencing the opposite behavior - seconds are excluded when they should be included and vice versa.

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest

---
Repository: /testbed
