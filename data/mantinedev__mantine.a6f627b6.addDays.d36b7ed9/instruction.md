# Bug Report

### Describe the bug

I'm experiencing an issue with the Heatmap component where the date range calculation seems to be off. When specifying a date range, the generated dates don't match what I expect - they appear to be shifted or incorrect.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

// When I try to generate a heatmap with a specific date range
// The dates that are displayed/calculated don't align properly

const startDate = new Date('2024-01-01');
const endDate = new Date('2024-01-07');

// Expected: 7 days from Jan 1 to Jan 7
// Actual: The dates seem to be calculated incorrectly
```

### Expected behavior

When providing a start and end date to the Heatmap component, the date range should be calculated correctly with proper day intervals. Each day should be exactly 24 hours apart and the total number of days should match the expected range.

### System Info
- @mantine/charts version: latest
- Browser: Chrome

---
Repository: /testbed
