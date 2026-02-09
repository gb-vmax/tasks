# Bug Report

### Describe the bug

The YearsList component is not displaying the first row of years correctly. When rendering a decade of years, the first 3 years are missing from the display, leaving the first row empty.

### Reproduction

```js
import { getYearsData } from '@mantine/dates';

// Try to get years data for a decade starting at 2020
const yearsData = getYearsData('2020-01-01');

console.log(yearsData);
// Expected: 4 rows with years distributed as [3, 3, 3, 1]
// Actual: First row is empty, years start from second row
```

### Expected behavior

The years should be distributed across 4 rows like this:
- Row 1: 2020, 2021, 2022
- Row 2: 2023, 2024, 2025
- Row 3: 2026, 2027, 2028
- Row 4: 2029

Instead, the first row is empty and all years are shifted down by one row.

### System Info

- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
