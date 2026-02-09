# Bug Report

### Describe the bug

When setting a `minDate` on a date picker component with a decade view, the year selection is incorrectly disabled. Years that should be selectable are being disabled, and the disabled state appears to be off by one year.

### Reproduction

```jsx
// Using a decade picker with minDate set
<DatePicker 
  decade="2022-04-11" 
  minDate="2023-05-11" 
/>
```

When rendering this component:
- The year 2020 should be disabled (before minDate) ✓
- The year 2021 should be disabled (before minDate) ✓  
- The year 2022 should be disabled (before minDate) ✓
- The year 2023 should be **enabled** (matches minDate year) ✗ Currently disabled
- Later years should be enabled ✓

### Expected behavior

Years that are greater than or equal to the `minDate` year should be selectable. In the example above, since `minDate` is set to "2023-05-11", the year 2023 and all subsequent years in the decade should be enabled for selection.

Currently, it seems like the first selectable year is 2024 instead of 2023, suggesting an off-by-one error in the year comparison logic.

### System Info
- Mantine version: latest
- React version: 18.x

---
Repository: /testbed
