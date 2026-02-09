# Bug Report

### Describe the bug

The months list is rendering incorrectly - I'm getting 4 months in the first 3 rows instead of the expected 3 months per row layout. The grid structure seems broken.

### Reproduction

```js
import { getMonthsData } from '@mantine/dates';

const monthsData = getMonthsData('2024');
console.log(monthsData);

// Current output structure:
// Row 0: [Jan, Feb, Mar, Apr] - 4 months
// Row 1: [May, Jun, Jul, Aug] - 4 months  
// Row 2: [Sep, Oct, Nov, Dec] - 4 months
// Row 3: [] - empty

// Expected output structure:
// Row 0: [Jan, Feb, Mar] - 3 months
// Row 1: [Apr, May, Jun] - 3 months
// Row 2: [Jul, Aug, Sep] - 3 months
// Row 3: [Oct, Nov, Dec] - 3 months
```

### Expected behavior

The months should be organized in a 4x3 grid (4 rows, 3 columns each) to properly display all 12 months of the year. Currently it's trying to fit 4 months in each row which breaks the layout and leaves the last row empty.

### System Info
- @mantine/dates version: latest
- Browser: Firefox 121

---
Repository: /testbed
