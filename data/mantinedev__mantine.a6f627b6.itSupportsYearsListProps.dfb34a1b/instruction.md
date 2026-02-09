# Bug Report

### Describe the bug

When using date picker components with `minDate` and `maxDate` props, the year selection doesn't properly disable years that fall outside the allowed range. Some years that should be disabled remain clickable, and some years that should be enabled are incorrectly disabled.

### Reproduction

```jsx
// Case 1: Years that should be enabled are disabled
<YearPicker 
  decade="2020-01-01" 
  minDate="2023-05-11" 
/>
// Expected: Year 2023 should be clickable
// Actual: Year 2023 is disabled

// Case 2: Years that should be disabled are enabled
<YearPicker 
  decade="2022-04-11" 
  maxDate="2023-05-11" 
/>
// Expected: Year 2024 should be disabled
// Actual: Year 2024 is clickable
```

### Expected behavior

Years should be properly disabled based on the `minDate` and `maxDate` constraints:
- When `minDate` is set, all years before the minimum year should be disabled
- When `maxDate` is set, all years after the maximum year should be disabled
- Years within the valid range should remain enabled

### System Info

- Mantine version: latest
- React version: 18.x

---
Repository: /testbed
