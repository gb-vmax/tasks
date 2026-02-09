# Bug Report

### Describe the bug

When using the date picker with `type="multiple"`, only the first selected date is displayed in the input field instead of showing all selected dates. Similarly, for `type="range"`, only the start date is shown even when both start and end dates are selected.

### Reproduction

```jsx
// Multiple dates - only first date shows
<DatePicker 
  type="multiple" 
  value={[new Date('2024-01-01'), new Date('2024-01-15'), new Date('2024-01-30')]} 
/>
// Expected: "Jan 1, 2024, Jan 15, 2024, Jan 30, 2024"
// Actual: "Jan 1, 2024"

// Range dates - only start date shows
<DatePicker 
  type="range" 
  value={[new Date('2024-01-01'), new Date('2024-01-31')]} 
/>
// Expected: "Jan 1, 2024 – Jan 31, 2024"
// Actual: "Jan 1, 2024"
```

### Expected behavior

- For `type="multiple"`: All selected dates should be displayed in the input, separated by commas
- For `type="range"`: Both start and end dates should be displayed with the separator between them

### System Info
- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
