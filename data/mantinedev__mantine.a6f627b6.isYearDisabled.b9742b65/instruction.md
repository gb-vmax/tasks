# Bug Report

### Describe the bug

The YearPicker component is incorrectly disabling years when using `minDate` or `maxDate` props. Years that should be selectable are being disabled, and years that should be disabled remain selectable.

### Reproduction

```jsx
import { YearPicker } from '@mantine/dates';

// Case 1: Only maxDate is set
<YearPicker maxDate={new Date(2025, 0, 1)} />
// Expected: Years after 2025 should be disabled
// Actual: All years are enabled

// Case 2: Only minDate is set  
<YearPicker minDate={new Date(2020, 0, 1)} />
// Expected: Years before 2020 should be disabled
// Actual: All years are enabled

// Case 3: Both minDate and maxDate are set
<YearPicker 
  minDate={new Date(2020, 0, 1)} 
  maxDate={new Date(2025, 0, 1)} 
/>
// Expected: Only years 2020-2025 should be selectable
// Actual: Years after 2025 are selectable, years before 2025 are disabled
```

### Expected behavior

- When `minDate` is set, years before that date should be disabled
- When `maxDate` is set, years after that date should be disabled  
- When both are set, only years within the range should be selectable

### System Info

- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
