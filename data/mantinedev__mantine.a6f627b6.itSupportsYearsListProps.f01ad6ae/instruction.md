# Bug Report

### Describe the bug

I'm experiencing an issue with the year picker where the disabled state of years doesn't match the expected behavior based on the `minDate` and `maxDate` props. Some years that should be disabled are still clickable, and vice versa.

### Reproduction

```jsx
import { YearPicker } from '@mantine/dates';

// Case 1: Years before minDate should be disabled
<YearPicker decade="2022-04-11" minDate="2023-05-11" />
// Expected: Years 2020, 2021, 2022, 2023 should be disabled
// Actual: Only some years are disabled, 2023 appears to be clickable

// Case 2: Years after maxDate should be disabled  
<YearPicker decade="2020-01-01" maxDate="2023-05-11" />
// Expected: Years 2024-2029 should be disabled
// Actual: Year 2024 is clickable when it shouldn't be
```

### Expected behavior

When `minDate` is set, all years before (and including partial years before) the minimum date should be disabled. Similarly, when `maxDate` is set, all years after (and including partial years after) the maximum date should be disabled.

The year picker should correctly identify which years fall outside the valid range and apply the disabled state accordingly.

### System Info
- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
