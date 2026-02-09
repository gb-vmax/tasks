# Bug Report

### Describe the bug

The `findClosestNumber` utility function is returning incorrect results when finding the closest number in an array. It seems to be comparing values incorrectly and not actually finding the number that's closest to the target value.

### Reproduction

```js
import { findClosestNumber } from '@mantine/core';

// Example 1: Should return 5, but returns wrong value
const result1 = findClosestNumber(6, [1, 5, 10]);
console.log(result1); // Expected: 5, but getting unexpected result

// Example 2: Should return 100
const result2 = findClosestNumber(95, [50, 100, 150]);
console.log(result2); // Expected: 100

// Example 3: When multiple numbers are equidistant
const result3 = findClosestNumber(5, [3, 7]);
console.log(result3); // Should consistently return one of them
```

### Expected behavior

The function should return the number from the array that has the smallest absolute difference from the target value. When two numbers are equidistant, it should return the first one encountered.

### System Info

- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
