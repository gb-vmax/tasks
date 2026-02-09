# Bug Report

### Describe the bug

The `findClosestNumber` utility function is returning incorrect values when working with arrays. When I pass an array with a single number, it returns my input value instead of the number from the array. Also, when there are multiple numbers equidistant from the target value, it's returning the last one instead of the first one.

### Reproduction

```js
import { findClosestNumber } from '@mantine/core';

// Case 1: Single element array
const result1 = findClosestNumber(10, [5]);
console.log(result1); // Expected: 5, Actual: 10

// Case 2: Equidistant values
const result2 = findClosestNumber(5, [3, 7]);
console.log(result2); // Expected: 3 (first match), Actual: 7 (last match)
```

### Expected behavior

- When the array contains a single element, that element should be returned
- When multiple numbers are equidistant from the target value, the first one encountered should be returned (consistent with typical "closest number" behavior)

### System Info

- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
