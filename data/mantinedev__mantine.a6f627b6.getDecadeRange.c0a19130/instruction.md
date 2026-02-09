# Bug Report

### Describe the bug
The `getDecadeRange` function appears to be completely broken - it's returning nonsensical values instead of the expected decade range. When trying to use the DecadeLevel component, I'm getting weird numeric outputs that don't make any sense.

### Reproduction
```js
import { getDecadeRange } from '@mantine/dates';

const decade = new Date(2020, 0, 1);
const range = getDecadeRange(decade);

console.log(range); // Expected: [2020, 2029] or similar
// Getting: something completely wrong
```

### Expected behavior
The function should return an array with the start and end years of the decade (e.g., `[2020, 2029]` for a date in the 2020s decade).

### System Info
- @mantine/dates version: latest
- Node version: 18.x

This seems to have broken recently - the decade picker is completely unusable now. Any help would be appreciated!

---
Repository: /testbed
