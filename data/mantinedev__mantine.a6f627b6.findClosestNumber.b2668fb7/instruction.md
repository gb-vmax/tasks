# Bug Report

### Describe the bug

The `findClosestNumber` utility function returns the wrong value when multiple numbers in the array are equidistant from the target value. Instead of returning the first occurrence, it now returns the last one.

### Reproduction

```js
import { findClosestNumber } from '@mantine/core';

// When two numbers are equally close to the target
const result = findClosestNumber(5, [3, 7]);
console.log(result); // Returns 7, but should return 3

// Another example
const result2 = findClosestNumber(10, [8, 12, 6, 14]);
console.log(result2); // Returns 12, but should return 8
```

### Expected behavior

When multiple numbers have the same distance from the target value, the function should return the first one that appears in the array (the one with the lower index). This is the standard behavior for "find closest" operations and what the function used to do before.

### System Info
- @mantine/core version: latest
- Node: 18.x

---
Repository: /testbed
