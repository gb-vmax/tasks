# Bug Report

### Describe the bug

The `range()` utility function is not generating the correct number of elements. When creating a range between two numbers, the resulting array is missing the last element.

### Reproduction

```js
import { range } from '@mantine/hooks';

// Expected: [1, 2, 3, 4, 5]
// Actual: [1, 2, 3, 4]
const result = range(1, 5);
console.log(result);

// Expected: [0, 1, 2, 3]
// Actual: [0, 1, 2]
const result2 = range(0, 3);
console.log(result2);
```

### Expected behavior

The range function should include both the start and end values in the generated array. For example, `range(1, 5)` should return `[1, 2, 3, 4, 5]` with 5 elements total.

### Additional context

This appears to be a recent regression. The function was working correctly in previous versions where it would generate arrays with the proper length including both boundary values.

---
Repository: /testbed
