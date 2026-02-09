# Bug Report

### Describe the bug

I'm experiencing an issue with the date range picker where the hidden input value is formatted incorrectly when only one date is selected. The behavior seems backwards - when I select just a start date, nothing appears in the hidden input, but when I select just an end date, it shows up correctly.

Also noticed that when using `type="multiple"`, the hidden input is showing dates that are `null` or `undefined` instead of filtering them out properly.

### Reproduction

```jsx
// Case 1: Range picker with only start date selected
<DatePickerInput type="range" value={[new Date(), null]} />
// Hidden input shows: "" (empty)
// Expected: "2024-01-15 –"

// Case 2: Range picker with only end date selected  
<DatePickerInput type="range" value={[null, new Date()]} />
// Hidden input shows: "– 2024-01-15" 
// Expected: "" (empty) or should handle this case

// Case 3: Multiple dates with null values
<DatePickerInput type="multiple" value={[new Date(), null, new Date()]} />
// Hidden input only shows the null values instead of the actual dates
```

### Expected behavior

- When only the start date is selected in a range, the hidden input should show "startDate –"
- When only the end date is selected, it should probably show empty or handle it appropriately
- For multiple dates, null/undefined values should be filtered out and only valid dates should appear in the comma-separated list

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
