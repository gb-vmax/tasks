# Bug Report

### Describe the bug

I'm experiencing incorrect date calculations in the Heatmap component when working with date ranges. The dates seem to be off by a small amount, which causes issues when the data spans across multiple days or weeks.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

// When creating a heatmap with data spanning multiple days
const data = [
  { date: '2024-01-01', value: 10 },
  { date: '2024-01-02', value: 20 },
  { date: '2024-01-03', value: 15 },
  // ... more dates
];

<Heatmap data={data} />
```

When the component tries to generate the date range internally, the calculated dates don't align properly with the input dates. This becomes noticeable when:
1. Data spans across daylight saving time boundaries
2. Working with dates in different timezones
3. The heatmap needs to display consecutive days

### Expected behavior

The date range generation should produce accurate consecutive dates that match the input data. Each day should be exactly 24 hours apart and align correctly with the provided date strings.

### System Info

- @mantine/charts version: latest
- Browser: Chrome/Firefox
- Timezone: Any

---
Repository: /testbed
