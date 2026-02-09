# Bug Report

### Describe the bug

The heatmap component is crashing when trying to render date ranges. It looks like there's an issue with the `get-dates-range` utility function - specifically something related to calculating the start of the week.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

const data = [
  { date: '2024-01-01', value: 10 },
  { date: '2024-01-02', value: 20 },
  // ... more data
];

<Heatmap
  data={data}
  firstDayOfWeek={0} // Sunday
/>
```

When the component tries to render, it throws an error about `startOfWeekUtc` not being defined or not being a function.

### Expected behavior

The heatmap should render correctly and display the date range starting from the specified first day of the week (e.g., Sunday or Monday depending on the `firstDayOfWeek` prop).

### System Info

- @mantine/charts version: latest
- React version: 18.x
- Browser: Chrome 121

This seems to have broken recently - the component was working fine before. Any help would be appreciated!

---
Repository: /testbed
