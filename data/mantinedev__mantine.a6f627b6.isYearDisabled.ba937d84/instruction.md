# Bug Report

### Describe the bug

When using `YearsList` component with `minDate` or `maxDate` props, the year selection behavior is incorrect. Years that should be selectable are being disabled, and the boundary years (the actual min/max years) are also incorrectly disabled.

### Reproduction

```jsx
import { YearsList } from '@mantine/dates';

// Case 1: Only minDate is set
<YearsList 
  minDate={new Date(2020, 0, 1)} 
/>
// Expected: Years 2020 and later should be selectable
// Actual: Year 2020 itself is disabled

// Case 2: Only maxDate is set
<YearsList 
  maxDate={new Date(2025, 11, 31)} 
/>
// Expected: Years 2025 and earlier should be selectable
// Actual: Year 2025 itself is disabled

// Case 3: Both minDate and maxDate are set
<YearsList 
  minDate={new Date(2020, 0, 1)}
  maxDate={new Date(2025, 11, 31)}
/>
// Expected: Years 2020-2025 should be selectable
// Actual: All years are selectable (no restrictions applied)
```

### Expected behavior

- When `minDate` is set to 2020, the year 2020 should be selectable (not disabled)
- When `maxDate` is set to 2025, the year 2025 should be selectable (not disabled)
- When both `minDate` and `maxDate` are set, only years within that range should be selectable
- The boundary years themselves should always be included in the selectable range

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest

---
Repository: /testbed
