# Bug Report

### Describe the bug

The months list is not displaying correctly - some months are missing and the grid layout appears broken. It looks like only certain months are being rendered instead of all 12 months of the year.

### Reproduction

```js
import { getMonthsData } from '@mantine/dates';

const monthsData = getMonthsData('2024');
console.log(monthsData);

// Expected: 4 rows with 3 months each (12 total months)
// Actual: Some rows are empty or missing months
```

When I try to render a months picker for any year, the grid doesn't show all 12 months. Some rows appear to be skipped entirely and within rows, months seem to be missing as well.

### Expected behavior

The `getMonthsData` function should return a 4x3 grid containing all 12 months of the year:
- Row 1: Jan, Feb, Mar
- Row 2: Apr, May, Jun  
- Row 3: Jul, Aug, Sep
- Row 4: Oct, Nov, Dec

### System Info

- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
