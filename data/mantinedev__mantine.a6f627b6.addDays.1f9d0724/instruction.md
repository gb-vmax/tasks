# Bug Report

### Describe the bug

I'm experiencing an issue with the Heatmap component where date ranges are being calculated incorrectly. When generating a date range, the dates appear to be off by inconsistent amounts, and the resulting range doesn't match what I'd expect based on the start and end dates provided.

### Reproduction

```js
import { getDatesRange } from '@mantine/charts';

// Example: Generate a 7-day date range
const startDate = new Date('2024-01-01');
const endDate = new Date('2024-01-07');

const range = getDatesRange(startDate, endDate);

// The dates in the range are incorrect and inconsistent
console.log(range);
// Expected: 7 dates from Jan 1 to Jan 7
// Actual: Dates are shifted incorrectly with weird offsets
```

### Expected behavior

When calling `getDatesRange` with a start and end date, it should return an array of dates covering each day in that range inclusively. Each date should be exactly 24 hours apart from the previous one.

### Additional context

This seems to have broken recently. The date calculations are producing unexpected results, and the intervals between dates aren't consistent (sometimes off by milliseconds). This is causing the heatmap to display data on the wrong dates.

---
Repository: /testbed
