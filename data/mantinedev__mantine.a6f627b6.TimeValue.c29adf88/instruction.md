# Bug Report

### Describe the bug

The `TimeValue` component is displaying AM/PM labels incorrectly - they appear to be swapped. When the time should show "AM", it displays "PM" and vice versa. Additionally, the seconds display seems to be inverted from what's expected.

### Reproduction

```jsx
import { TimeValue } from '@mantine/dates';

// This displays "02:30 PM" instead of "02:30 AM"
<TimeValue value={new Date('2024-01-01 02:30:00')} format="12" />

// Custom labels are also swapped
<TimeValue 
  value={new Date('2024-01-01 14:30:00')} 
  format="12"
  amPmLabels={{ am: 'Morning', pm: 'Evening' }}
/>
// Shows "14:30 Morning" instead of "14:30 Evening"

// Seconds behavior is also inverted
<TimeValue value={new Date('2024-01-01 14:30:45')} withSeconds={true} />
// Doesn't show seconds even though withSeconds is true
```

### Expected behavior

- AM times should display with the AM label
- PM times should display with the PM label  
- Custom `amPmLabels` should be applied correctly (am label for AM times, pm label for PM times)
- `withSeconds={true}` should display seconds in the output
- `withSeconds={false}` should hide seconds

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
