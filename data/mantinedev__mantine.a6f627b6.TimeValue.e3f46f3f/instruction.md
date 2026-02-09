# Bug Report

### Describe the bug

When using the `TimeValue` component with `withSeconds` prop, the time format and AM/PM labels are being overridden incorrectly. Setting `withSeconds={true}` forces the format to always be `'12h'` and changes the AM/PM labels to lowercase, ignoring any custom `format` or `amPmLabels` props that were passed.

### Reproduction

```jsx
import { TimeValue } from '@mantine/dates';

// Example 1: Custom format is ignored when withSeconds is true
<TimeValue 
  value={new Date()} 
  format="24h"
  withSeconds={true}
/>
// Expected: 24-hour format with seconds
// Actual: 12-hour format with seconds (format prop ignored)

// Example 2: Custom amPmLabels are ignored when withSeconds is true
<TimeValue 
  value={new Date()} 
  amPmLabels={{ am: 'AM', pm: 'PM' }}
  withSeconds={true}
/>
// Expected: Uses custom 'AM'/'PM' labels
// Actual: Uses lowercase 'am'/'pm' labels (amPmLabels prop ignored)
```

### Expected behavior

The `withSeconds` prop should only control whether seconds are displayed or not. It should not override the `format` or `amPmLabels` props. When I pass custom values for these props, they should be respected regardless of the `withSeconds` value.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
