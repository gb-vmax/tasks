# Bug Report

### Describe the bug

I'm experiencing an issue with the `HiddenDatesInput` component when working with date ranges. When I select a date range where the start date is set but the end date is missing, the formatted output is showing incorrectly. Instead of displaying the start date followed by a dash (like "2024-01-15 –"), it seems to be checking the wrong date value.

Also noticed that when using the `multiple` date type with an array of dates, the output is completely wrong - it's showing empty/null values instead of the actual selected dates.

### Reproduction

```jsx
// Case 1: Date range with missing end date
<HiddenDatesInput 
  type="range"
  value={[new Date('2024-01-15'), null]}
/>
// Expected: "2024-01-15 –"
// Getting: Wrong output or empty string

// Case 2: Multiple dates selection
<HiddenDatesInput 
  type="multiple"
  value={[new Date('2024-01-15'), new Date('2024-01-20'), new Date('2024-01-25')]}
/>
// Expected: "2024-01-15, 2024-01-20, 2024-01-25"
// Getting: Empty strings or missing dates
```

### Expected behavior

1. For date ranges with only a start date, it should display the start date followed by " –"
2. For multiple date selections, all valid dates should be displayed, separated by commas

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
