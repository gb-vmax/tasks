# Bug Report

### Describe the bug

The Heatmap component is not rendering month boundaries correctly when there are gaps in the data. When I have a heatmap with some months that have null values, the month labels are disappearing or showing incorrectly.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

const data = [
  { date: '2024-01-01', value: 10 },
  { date: '2024-01-15', value: 20 },
  // February has no data (null months)
  { date: '2024-03-01', value: 15 },
  { date: '2024-03-10', value: 25 },
];

<Heatmap data={data} />
```

### Expected behavior

The heatmap should show month labels for January and March, with February being handled gracefully even though it has no data. The month boundaries should be calculated correctly and the next non-null month should be identified properly.

### Actual behavior

Month labels are not appearing correctly. It seems like the logic for finding the next month after a gap in data is broken - the component stops looking for the next valid month as soon as it encounters a null value instead of continuing to search.

### System Info

- @mantine/charts version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
