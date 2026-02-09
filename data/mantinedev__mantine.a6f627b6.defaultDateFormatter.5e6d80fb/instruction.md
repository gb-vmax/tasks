# Bug Report

### Describe the bug

The date range formatter is showing incorrect output when only a start date is selected. Instead of displaying the start date with the separator (e.g., "Jan 1, 2024 – "), it's not showing anything at all.

Also noticed that for multiple date selection, the dates are now separated by spaces instead of commas and spaces, which looks wrong.

### Reproduction

```js
// Range picker - selecting only start date
const rangeDate = [new Date('2024-01-01'), null];
const formatted = defaultDateFormatter({
  date: rangeDate,
  type: 'range',
  locale: 'en',
  format: 'MMM DD, YYYY',
  labelSeparator: '–'
});
// Expected: "Jan 1, 2024 – "
// Actual: nothing is displayed

// Multiple date picker
const multipleDates = [new Date('2024-01-01'), new Date('2024-01-15')];
const formattedMultiple = defaultDateFormatter({
  date: multipleDates,
  type: 'multiple',
  locale: 'en',
  format: 'MMM DD, YYYY'
});
// Expected: "Jan 1, 2024, Jan 15, 2024"
// Actual: "Jan 1, 2024 Jan 15, 2024" (missing comma)
```

### Expected behavior

1. For range pickers: When only the start date is selected, it should display the start date followed by the separator (e.g., "Jan 1, 2024 – ")
2. For multiple date pickers: Selected dates should be separated by ", " (comma and space), not just a space

### System Info
- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
