# Bug Report

### Describe the bug

The `findClosestNumber` utility function is returning unexpected results when there are multiple numbers equidistant from the target value. It seems to be returning the last matching number instead of the first one found in the array.

### Reproduction

```js
import { findClosestNumber } from '@mantine/core';

// When two numbers are equally close to the target
const numbers = [10, 20, 30];
const result = findClosestNumber(25, numbers);

console.log(result); // Returns 30, but should return 20
```

Another example:
```js
const numbers = [5, 15, 25];
const result = findClosestNumber(10, numbers);

console.log(result); // Returns 15 instead of 5
```

### Expected behavior

When multiple numbers are equidistant from the target value, the function should return the first one encountered in the array (the one with the lower index), not the last one.

In the first example above, both 20 and 30 are 5 units away from 25, so it should return 20 since it appears first.

### System Info
- @mantine/core version: latest
- Browser: N/A (occurs in all environments)

---
Repository: /testbed
