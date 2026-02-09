# Bug Report

### Describe the bug

The `getDecadeRange` function is returning incorrect year values for decade ranges. When I try to get the decade range for a given date, the returned start and end years don't match the actual decade boundaries.

### Reproduction

```js
import { getDecadeRange } from '@mantine/dates';

// Try to get the decade range for a date in the 2020s
const range = getDecadeRange(new Date(2020, 0, 1));

// Expected: [2020, 2029] or similar decade boundaries
// Actual: Returns wrong years that don't represent the decade correctly
console.log(range);
```

The function seems to be picking the wrong indices from the years array, causing it to return years that don't correspond to the start and end of the decade.

### Expected behavior

The function should return the correct start and end years for the decade containing the given date. For example, if I pass a date in 2020, it should return something like `[2020, 2029]` representing the full decade range.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
