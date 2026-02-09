# Bug Report

### Describe the bug

The `getDecadeRange` function is returning incorrect year boundaries for a decade. When I call this function, it's returning years from the middle of the decade instead of the first and last years.

### Reproduction

```js
import { getDecadeRange } from '@mantine/dates';

// For a decade starting in 2020
const range = getDecadeRange(new Date(2020, 0, 1));

// Expected: [2020, 2029] (first and last year of the decade)
// Actual: returns middle years instead of the decade boundaries
console.log(range);
```

### Expected behavior

The function should return the first and last year of the decade (e.g., for 2020s it should return 2020 and 2029), but it's currently returning years from somewhere in the middle of the decade range.

### System Info

- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
