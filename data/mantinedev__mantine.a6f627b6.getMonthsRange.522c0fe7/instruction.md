# Bug Report

### Describe the bug

I'm experiencing an issue with the Heatmap component where the month labels are positioned incorrectly when rendering calendar data. The month ranges appear to be calculated with an off-by-one error, causing the labels to not align properly with their corresponding weeks.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

const weeksData = [
  ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07'],
  ['2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14'],
  // ... more weeks
  ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-04', null, null, null],
];

<Heatmap data={weeksData} />
```

When the heatmap renders, the month labels don't line up correctly with the actual month boundaries in the data. It seems like the logic for determining which day to use for month calculation is reversed - it's picking the wrong end of the week when there are null values.

### Expected behavior

Month labels should align correctly with the first occurrence of each month in the calendar data, even when weeks contain null values at the beginning or end.

### System Info
- @mantine/charts version: latest
- Browser: Chrome 120

---
Repository: /testbed
