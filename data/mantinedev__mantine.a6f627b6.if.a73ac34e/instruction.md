# Bug Report

### Describe the bug

When using the Heatmap component without `splitMonths` enabled, the month labels are being assigned incorrectly. The component appears to be determining the month based on the wrong day in each week, causing month labels to be misaligned or incorrect.

### Reproduction

```jsx
import { Heatmap } from '@mantine/charts';

const data = [
  // Weekly data spanning multiple months
  { date: '2024-01-28', value: 5 },
  { date: '2024-01-29', value: 3 },
  { date: '2024-02-01', value: 8 }, // Week crosses into February
  { date: '2024-02-02', value: 4 },
  // ... more data
];

// Render heatmap without splitMonths
<Heatmap data={data} splitMonths={false} />
```

### Expected behavior

When a week contains dates from different months, the month label should be determined consistently. Currently experiencing issues where weeks that span month boundaries get labeled with the wrong month, particularly noticeable when the first few days of a week are in one month and the remaining days are in another.

### System Info

- @mantine/charts version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
