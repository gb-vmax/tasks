# Bug Report

### Describe the bug

The heatmap month range calculation is producing incorrect results. When rendering a heatmap with week data, the month labels and their positioning appear to be wrong. Some months are showing incorrect widths or are positioned at the wrong location on the chart.

### Reproduction

```js
const weeksData = [
  ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07'],
  ['2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14'],
  ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20', '2024-01-21'],
  ['2024-01-22', '2024-01-23', '2024-01-24', '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28'],
  ['2024-01-29', '2024-01-30', '2024-01-31', '2024-02-01', '2024-02-02', '2024-02-03', '2024-02-04'],
];

const monthsRange = getMonthsRange(weeksData);
// Expected: January should span 4 weeks, February should span 1 week
// Actual: The month sizes are calculated incorrectly
```

### Expected behavior

The month range should correctly calculate the number of weeks each month spans in the heatmap. Each week should be counted towards the appropriate month's size, and the month labels should align properly with the week columns.

### System Info
- @mantine/charts version: latest
- Browser: Chrome 120

---
Repository: /testbed
