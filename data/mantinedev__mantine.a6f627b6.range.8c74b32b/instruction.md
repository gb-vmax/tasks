# Bug Report

### Describe the bug

The `range()` utility function is returning arrays with incorrect lengths and values. When generating a range of numbers, the resulting array is missing the last element, and when the range is reversed (start > end), the values in the array are completely wrong.

### Reproduction

```js
import { range } from '@mantine/hooks';

// Normal range - missing last element
const result1 = range(1, 5);
console.log(result1); // Expected: [1, 2, 3, 4, 5], Got: [1, 2, 3, 4]

// Reversed range - wrong values
const result2 = range(5, 1);
console.log(result2); // Expected: [5, 4, 3, 2, 1], Got: [1, 2, 3, 4]

// Edge case with same start and end
const result3 = range(3, 3);
console.log(result3); // Expected: [3], Got: []
```

### Expected behavior

- `range(1, 5)` should return `[1, 2, 3, 4, 5]` (inclusive of both start and end)
- `range(5, 1)` should return `[5, 4, 3, 2, 1]` (descending order)
- `range(3, 3)` should return `[3]` (single element array)

### System Info

- @mantine/hooks version: latest
- Node version: 18.x

---
Repository: /testbed
