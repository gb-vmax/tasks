# Bug Report

### Describe the bug

The `TimeValue` component is displaying incorrect time formats. When using the component with `withSeconds` enabled, it shows an invalid format instead of the expected time with seconds. Additionally, when using 12-hour format, the AM/PM labels appear to be swapped - times that should show "AM" are showing "PM" and vice versa.

### Reproduction

```jsx
import { TimeValue } from '@mantine/dates';

// Case 1: With seconds enabled
<TimeValue 
  value={new Date('2024-01-01 14:30:45')} 
  withSeconds={true}
/>
// Expected: 14:30:45
// Actual: Shows invalid format

// Case 2: 12-hour format with AM/PM
<TimeValue 
  value={new Date('2024-01-01 09:30:00')} 
  format="12h"
  amPmLabels={{ am: 'AM', pm: 'PM' }}
/>
// Expected: 9:30 AM
// Actual: 9:30 PM (labels are swapped)
```

### Expected behavior

1. When `withSeconds` is enabled, the component should display the time including seconds in the proper format
2. When using 12-hour format, AM/PM labels should be displayed correctly (morning times show AM, afternoon/evening times show PM)

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
