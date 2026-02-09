# Bug Report

### Describe the bug

I'm experiencing an issue with the Heatmap component where the month labels are displaying incorrectly when `splitMonths` is set to `false`. Instead of showing the month of the first day in each week, it appears to be using the last day of the week for determining the month label.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

// Data with a week that spans across two months
const datesRange = [
  ['2024-01-29', '2024-01-30', '2024-01-31', '2024-02-01', '2024-02-02', '2024-02-03', '2024-02-04']
];

<Heatmap 
  data={myData}
  datesRange={datesRange}
  splitMonths={false}
/>
```

In this case, the week starts in January (Jan 29-31) but the component labels it as February because it's picking up the last day instead of the first day of the week.

### Expected behavior

The month label should be determined by the **first non-null day** in the week, not the last one. So a week starting on January 29th should be labeled as January, even if most of the days fall in February.

### System Info
- @mantine/charts version: latest
- Browser: Chrome

---
Repository: /testbed
