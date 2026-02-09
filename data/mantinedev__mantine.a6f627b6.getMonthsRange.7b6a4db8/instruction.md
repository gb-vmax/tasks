# Bug Report

### Describe the bug

The Heatmap component is displaying incorrect month labels/ranges when rendering calendar data. The month boundaries appear to be shifted or misaligned with the actual week data.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

// Sample data with weeks spanning multiple months
const data = [
  { date: '2024-01-01', value: 5 },
  { date: '2024-01-08', value: 3 },
  // ... more dates spanning January to February
  { date: '2024-02-01', value: 7 },
  { date: '2024-02-08', value: 2 },
];

<Heatmap data={data} />
```

When the heatmap renders, the month labels don't align correctly with the weeks. For example, weeks that should be labeled as "January" might show up under "February" or vice versa.

### Expected behavior

Month ranges should correctly correspond to the weeks they contain. If a week starts in January but ends in February, it should be associated with the appropriate month based on the week's position in the data.

### System Info

- @mantine/charts version: latest
- Browser: Chrome 120

---
Repository: /testbed
