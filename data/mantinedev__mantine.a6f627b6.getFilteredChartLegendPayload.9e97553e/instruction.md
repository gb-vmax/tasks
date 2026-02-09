# Bug Report

### Describe the bug

When using `ChartLegend`, items with `color !== 'none'` are being filtered out incorrectly. It appears that the legend is now showing items that should be hidden (those with `color: 'none'` or no color property) instead of showing items that have actual color values.

### Reproduction

```jsx
const data = [
  { name: 'Series 1', color: '#ff0000' },
  { name: 'Series 2', color: 'none' },
  { name: 'Series 3', color: '#00ff00' }
];

// After filtering, Series 1 and Series 3 should appear in the legend
// but instead only Series 2 (with color: 'none') is showing
```

### Expected behavior

The chart legend should display only items that have valid color values (i.e., colors that are NOT 'none' and NOT undefined/null). Items with `color: 'none'` or missing color properties should be filtered out and not appear in the legend.

### System Info
- @mantine/charts version: latest
- React version: 18.x

---
Repository: /testbed
