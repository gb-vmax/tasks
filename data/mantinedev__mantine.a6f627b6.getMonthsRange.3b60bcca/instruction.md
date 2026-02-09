# Bug Report

### Describe the bug

The heatmap chart is displaying incorrect month ranges and widths. When rendering a heatmap with weekly data, the month labels appear to be positioned incorrectly and some months are taking up more space than they should.

### Reproduction

```js
const weeksData = [
  ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07'],
  ['2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14'],
  // ... more weeks
  ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-04', '2024-02-05', '2024-02-06', '2024-02-07'],
];

// When getMonthsRange is called internally
// The month sizes are doubled (each week counts as 2 instead of 1)
// Also weeks starting with null values use the wrong day for month calculation
```

### Expected behavior

Each week should contribute a size of 1 to the month range, not 2. The month widths should accurately represent the number of weeks in that month. Additionally, when a week starts with a null value (partial week), it should use the first non-null day to determine which month it belongs to.

### System Info
- @mantine/charts version: latest
- Browser: Chrome

---
Repository: /testbed
