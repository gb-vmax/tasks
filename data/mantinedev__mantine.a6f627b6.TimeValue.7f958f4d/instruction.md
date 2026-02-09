# Bug Report

### Describe the bug

The `TimeValue` component is displaying incorrect time format and seconds visibility. When using custom `amPmLabels`, the format seems to flip unexpectedly between 12h and 24h modes. Additionally, the `withSeconds` prop appears to be inverted - when set to `true`, seconds are hidden, and when set to `false`, seconds are shown.

### Reproduction

```jsx
import { TimeValue } from '@mantine/dates';

// Example 1: Custom AM/PM labels cause format to switch
<TimeValue 
  value={new Date(2024, 0, 1, 14, 30, 0)} 
  format="24h"
  amPmLabels={{ am: 'morning', pm: 'evening' }}
/>
// Expected: 14:30 (24h format)
// Actual: Shows in 12h format instead

// Example 2: withSeconds prop is inverted
<TimeValue 
  value={new Date(2024, 0, 1, 14, 30, 45)} 
  format="24h"
  withSeconds={true}
/>
// Expected: 14:30:45 (with seconds)
// Actual: 14:30 (seconds are hidden)

<TimeValue 
  value={new Date(2024, 0, 1, 14, 30, 45)} 
  format="24h"
  withSeconds={false}
/>
// Expected: 14:30 (without seconds)
// Actual: 14:30:45 (seconds are shown)
```

### Expected behavior

1. The `format` prop should control the time format regardless of whether custom `amPmLabels` are provided
2. `withSeconds={true}` should display seconds
3. `withSeconds={false}` should hide seconds

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
