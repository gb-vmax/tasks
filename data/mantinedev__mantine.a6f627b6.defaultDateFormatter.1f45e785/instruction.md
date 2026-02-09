# Bug Report

### Describe the bug

When using date inputs with `type="multiple"`, the component is showing an empty string instead of the formatted dates. Also, for `type="range"`, the formatter is displaying the separator even when only one date is selected (either start or end date), which looks incorrect.

### Reproduction

```js
// Multiple dates case
const multipleDates = ['2024-01-15', '2024-01-20', '2024-01-25'];
// Expected: "Jan 15, 2024, Jan 20, 2024, Jan 25, 2024"
// Actual: "" (empty string)

// Range with only start date
const rangeWithStart = ['2024-01-15', null];
// Expected: "Jan 15, 2024" or no separator shown
// Actual: "Jan 15, 2024 – null" (separator shown with null)

// Range with only end date  
const rangeWithEnd = [null, '2024-01-20'];
// Expected: "Jan 20, 2024" or no separator shown
// Actual: "null – Jan 20, 2024" (separator shown with null)
```

### Expected behavior

- For multiple dates: Should display all selected dates joined with commas
- For range dates: Should only show the separator when both start and end dates are present, not when only one date is selected

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
