# Bug Report

### Describe the bug

The `range` utility function is producing incorrect results when generating number sequences. It seems to be returning arrays with wrong lengths and in some cases reversing when it shouldn't.

### Reproduction

```js
import { range } from '@mantine/hooks';

// Expected: [1, 2, 3, 4, 5]
// Getting wrong output
console.log(range(1, 5));

// Expected: [5, 4, 3, 2, 1]
// Getting wrong output
console.log(range(5, 1));

// The length is also off by one in some cases
console.log(range(0, 10)); // Should have 11 elements but doesn't
```

### Expected behavior

- `range(1, 5)` should return `[1, 2, 3, 4, 5]`
- `range(5, 1)` should return `[5, 4, 3, 2, 1]` (descending order)
- The length should include both start and end values

### System Info

- @mantine/hooks version: latest
- Node: 18.x

---
Repository: /testbed
