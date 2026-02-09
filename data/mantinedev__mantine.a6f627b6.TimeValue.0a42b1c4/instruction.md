# Bug Report

### Describe the bug

When using the `TimeValue` component with `withSeconds={true}`, the AM/PM labels are being swapped. Times that should display "AM" are showing "PM" and vice versa.

### Reproduction

```jsx
import { TimeValue } from '@mantine/dates';

// This displays "10:30:45 PM" when it should show "10:30:45 AM"
<TimeValue 
  value={new Date('2024-01-01 10:30:45')} 
  format="12" 
  withSeconds={true}
/>

// This displays "02:15:30 AM" when it should show "02:15:30 PM"
<TimeValue 
  value={new Date('2024-01-01 14:15:30')} 
  format="12" 
  withSeconds={true}
/>
```

### Expected behavior

The component should display the correct AM/PM labels regardless of whether `withSeconds` is enabled or not. Morning times (before noon) should show "AM" and afternoon/evening times (noon and after) should show "PM".

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
