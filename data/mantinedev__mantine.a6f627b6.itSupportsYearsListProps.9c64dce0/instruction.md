# Bug Report

### Describe the bug

The `minDate` and `maxDate` props are not correctly disabling years in the decade picker. When setting a `minDate`, years that should be disabled (before the minimum date) are actually enabled, and vice versa. The same issue occurs with `maxDate` where years after the maximum date remain enabled when they should be disabled.

### Reproduction

```tsx
// With minDate - years before 2023 should be disabled but are not
<YearPicker decade="2022-04-11" minDate="2023-05-11" />
// Expected: 2020, 2021, 2022 disabled
// Actual: 2020, 2021, 2022 enabled, 2023 disabled

// With maxDate - years after 2023 should be disabled but are not  
<YearPicker decade="2022-04-11" maxDate="2023-05-11" />
// Expected: 2024-2029 disabled
// Actual: 2023 disabled instead
```

### Expected behavior

When `minDate` is set, all years before that date should be disabled in the year picker. When `maxDate` is set, all years after that date should be disabled. The boundary year containing the min/max date should remain enabled.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
