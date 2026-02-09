# Bug Report

### Describe the bug

The `findClosestNumber` utility function is returning incorrect results when trying to find the closest number in an array to a given value. It seems to be comparing numbers incorrectly and not actually finding the closest match.

### Reproduction

```js
import { findClosestNumber } from '@mantine/core';

// Example 1: Should return 5 but returns wrong value
const result1 = findClosestNumber(6, [1, 5, 10]);
console.log(result1); // Expected: 5, but getting unexpected result

// Example 2: Should return 100 but returns wrong value  
const result2 = findClosestNumber(95, [50, 100, 150]);
console.log(result2); // Expected: 100, but getting unexpected result

// Example 3: Should return 0 but returns wrong value
const result3 = findClosestNumber(1, [-5, 0, 10]);
console.log(result3); // Expected: 0, but getting unexpected result
```

### Expected behavior

The function should return the number from the array that has the smallest absolute difference from the target value. For example, when looking for the closest number to 6 in `[1, 5, 10]`, it should return 5 since `|6-5| = 1` is smaller than both `|6-1| = 5` and `|6-10| = 4`.

### System Info
- @mantine/core version: latest
- Browser: N/A (utility function)

---
Repository: /testbed
