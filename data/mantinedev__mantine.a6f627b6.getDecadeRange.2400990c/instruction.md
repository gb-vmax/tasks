# Bug Report

### Describe the bug

The `getDecadeRange` function is returning incorrect start and end years for a decade. When querying the decade range, the returned values don't match the actual first and last years of the decade.

### Reproduction

```js
import { getDecadeRange } from '@mantine/dates';

// For a decade starting in 2020
const range = getDecadeRange(new Date(2020, 0, 1));
console.log(range); // Expected: [2020, 2029], but getting wrong values

// The start year is off and the end year doesn't match the last year of the decade
```

### Expected behavior

`getDecadeRange` should return an array with the first year and last year of the decade. For example:
- For 2020-2029 decade, it should return `[2020, 2029]`
- For 2010-2019 decade, it should return `[2010, 2019]`

Currently the function seems to be picking the wrong indices from the years data array, resulting in incorrect decade boundaries.

### System Info
- @mantine/dates version: latest
- Browser: N/A (affects all environments)

---
Repository: /testbed
