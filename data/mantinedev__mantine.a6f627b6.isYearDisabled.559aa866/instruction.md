# Bug Report

### Describe the bug

When using the YearsList component with `minDate` or `maxDate` props, the year selection behavior is incorrect. Years that should be selectable are being disabled, and years that should be disabled are selectable.

### Reproduction

```jsx
import { YearsList } from '@mantine/dates';

// Set minDate to 2020
<YearsList minDate={new Date(2020, 0, 1)} />

// Expected: Years before 2020 should be disabled
// Actual: Years after 2020 are disabled instead
```

Another case:
```jsx
// Set only maxDate
<YearsList maxDate={new Date(2025, 0, 1)} />

// Expected: Years after 2025 should be disabled
// Actual: All years are selectable (no restrictions applied)
```

### Expected behavior

- When `minDate` is set, years **before** the minimum date should be disabled
- When `maxDate` is set, years **after** the maximum date should be disabled  
- When only one of `minDate` or `maxDate` is provided, the restriction should still apply correctly

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
