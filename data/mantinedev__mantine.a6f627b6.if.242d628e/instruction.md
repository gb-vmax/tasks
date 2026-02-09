# Bug Report

### Describe the bug

I'm experiencing an issue with the Heatmap component where spacers between months are appearing in the wrong places. Instead of showing spacers when the month changes between adjacent columns, they're now appearing within the same month, which creates incorrect visual separation in the heatmap.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

// Create a heatmap with data spanning multiple months
const data = [
  { date: '2024-01-15', value: 5 },
  { date: '2024-01-20', value: 3 },
  { date: '2024-02-01', value: 8 },
  { date: '2024-02-05', value: 6 },
];

<Heatmap data={data} />
```

### Expected behavior

Spacers should only appear between columns when transitioning from one month to another (e.g., between January and February). Currently, spacers are being inserted incorrectly within the same month, breaking the visual grouping of data by month.

### System Info
- @mantine/charts version: latest
- Browser: Chrome 120

---
Repository: /testbed
