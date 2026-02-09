# Bug Report

### Describe the bug
When using date picker components with `minDate` prop, years that should be disabled are actually enabled, and vice versa. The `minDate` validation seems to be inverted - years before the minimum date are clickable while years after (which should be valid) are disabled.

### Reproduction
```jsx
// Example with decade picker
<YearPicker decade="2022-04-11" minDate="2023-05-11" />

// Years 2020, 2021, 2022 should be disabled (before minDate)
// But they are currently enabled and clickable

// Years 2023-2029 should be enabled (after minDate)  
// But they are currently disabled
```

### Expected behavior
- Years before `minDate` should be disabled and not selectable
- Years equal to or after `minDate` should be enabled and selectable
- The validation logic should prevent users from selecting dates that are before the specified minimum date

### System Info
- Mantine version: latest
- Component: YearPicker / date components with years list

This seems to affect all date picker components that support the `minDate` prop and display a list of years. The behavior is completely reversed from what would be expected.

---
Repository: /testbed
