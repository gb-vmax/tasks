# Bug Report

### Describe the bug
When sorting arrays of numbers using `ascendingNumberSort`, duplicate values are not being handled correctly. The sort function seems to be removing or incorrectly positioning duplicate numbers in the sorted output.

### Reproduction
```js
const numbers = [5, 2, 8, 2, 1, 5, 3];
const sorted = numbers.sort(ascendingNumberSort);

// Expected: [1, 2, 2, 3, 5, 5, 8]
// Actual: Some duplicate values are missing or in wrong positions
```

### Expected behavior
The sorting function should maintain all duplicate values in the array and position them correctly in ascending order. All instances of duplicate numbers should appear consecutively in the sorted result.

### System Info
- Version: latest
- Environment: Node.js

---
Repository: /testbed
