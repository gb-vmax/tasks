# Bug Report

### Describe the bug

The `getDecadeRange` function is returning incorrect start and end years for a decade. When I try to get the decade range, the values returned don't represent the actual first and last years of the decade.

### Reproduction

```js
import { getDecadeRange } from '@mantine/dates';

// Try to get the decade range for 2020s
const range = getDecadeRange(new Date(2020, 0, 1));

// Expected: [2020, 2029]
// Actual: Returns wrong years from the decade
console.log(range);
```

The function seems to be accessing the wrong indices from the years data array, causing it to return years that aren't the boundaries of the decade.

### Expected behavior

`getDecadeRange` should return a tuple with the first year and last year of the decade. For example, for the 2020s decade, it should return `[2020, 2029]`.

### System Info
- @mantine/dates version: latest
- Framework: React

---
Repository: /testbed
