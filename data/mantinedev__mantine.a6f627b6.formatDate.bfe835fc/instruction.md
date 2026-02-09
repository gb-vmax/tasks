# Bug Report

### Describe the bug

The heatmap component is generating incorrect date strings. When displaying dates, the year appears to be off by 1900 years and single-digit days are not being padded correctly with leading zeros.

### Reproduction

```js
// Create a heatmap with date data
const data = [
  { date: '2024-01-05', value: 10 },
  { date: '2024-01-06', value: 15 }
];

// The dates are being formatted incorrectly
// Expected: '2024-01-05'
// Getting: '124-01-5' (year is 2024-1900=124, day has no zero padding)
```

### Expected behavior

Dates should be formatted correctly with:
- The actual year (e.g., 2024, not 124)
- Day numbers padded to 2 digits with leading zeros (e.g., '05' not '5')

### System Info
- @mantine/charts version: latest
- Browser: Chrome

This is breaking our heatmap visualizations as the date strings are malformed. Any help would be appreciated!

---
Repository: /testbed
