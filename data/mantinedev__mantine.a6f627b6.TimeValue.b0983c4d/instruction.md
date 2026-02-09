# Bug Report

### Describe the bug

The `TimeValue` component is displaying time incorrectly. When using the component with AM/PM labels, the labels appear to be swapped - times that should show "AM" are showing "PM" and vice versa. Additionally, the `withSeconds` prop seems to be behaving in reverse of what's expected.

### Reproduction

```jsx
import { TimeValue } from '@mantine/dates';

// Example 1: AM/PM labels are swapped
<TimeValue 
  value={new Date('2024-01-01 09:30:00')} 
  format="12h"
  amPmLabels={{ am: 'AM', pm: 'PM' }}
/>
// Expected: "9:30 AM"
// Actual: Shows "9:30 PM"

// Example 2: withSeconds behaves inversely
<TimeValue 
  value={new Date('2024-01-01 14:30:45')} 
  format="24h"
  withSeconds={true}
/>
// Expected: Should show seconds (14:30:45)
// Actual: Doesn't show seconds (14:30)

<TimeValue 
  value={new Date('2024-01-01 14:30:45')} 
  format="24h"
  withSeconds={false}
/>
// Expected: Should NOT show seconds (14:30)
// Actual: Shows seconds (14:30:45)
```

### Expected behavior

- When `format="12h"`, AM/PM labels should display correctly (morning times show AM, afternoon/evening times show PM)
- When `withSeconds={true}`, the time should include seconds
- When `withSeconds={false}`, the time should not include seconds
- The behavior should be consistent regardless of the time format used

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
