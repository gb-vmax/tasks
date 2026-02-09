# Bug Report

### Describe the bug

When using date picker components with `minDate` prop, the year selection is incorrectly disabling years that should be selectable. Specifically, when setting a minimum date, the third year in the decade view is being disabled even though it's within the valid range.

### Reproduction

```jsx
<DatePicker 
  decade="2020-01-01" 
  minDate="2022-01-01" 
/>
```

When the decade view is rendered, the years 2020 and 2021 are correctly disabled (as they're before minDate), but 2022 is also disabled even though it matches the minDate year and should be selectable.

### Expected behavior

Only years that are strictly before the `minDate` year should be disabled. The year matching `minDate` should be enabled and selectable.

In the example above with `minDate="2022-01-01"`:
- 2020 should be disabled ✓
- 2021 should be disabled ✓  
- 2022 should be **enabled** ✗ (currently disabled)
- 2023+ should be enabled ✓

### System Info
- Mantine version: latest
- React version: 18.x

---
Repository: /testbed
