# Bug Report

### Describe the bug

The Heatmap component is generating incorrect date strings when processing date ranges. The dates appear to be formatted incorrectly, showing wrong month and day values.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

const data = [
  { date: '2024-01-15', value: 10 },
  { date: '2024-02-20', value: 15 },
  { date: '2024-03-25', value: 20 }
];

// When rendering the heatmap, the dates don't match the input
<Heatmap data={data} />
```

When I pass in dates like `2024-01-15` (January 15th), the heatmap seems to be displaying them with incorrect formatting. The month appears to be off by one (showing December instead of January), and the day values don't correspond to the actual day of the month.

### Expected behavior

The heatmap should correctly format and display the dates as provided in the data. A date like `2024-01-15` should be processed and displayed as January 15th, 2024.

### Additional context

This seems to affect the date range generation internally. The visual representation on the heatmap doesn't align with the actual dates in my dataset, making it confusing to interpret the data.

---
Repository: /testbed
