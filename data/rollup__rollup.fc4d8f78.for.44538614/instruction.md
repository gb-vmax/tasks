# Bug Report

### Describe the bug

The `concatLazy` function is not concatenating iterables correctly. When passing multiple iterables, only the first element from each iterable (starting from the second one) is yielded, and the first iterable is completely skipped.

### Reproduction

```js
const iter1 = [1, 2, 3];
const iter2 = [4, 5, 6];
const iter3 = [7, 8, 9];

const result = [...concatLazy([iter1, iter2, iter3])];
console.log(result);
// Actual output: [4, 7]
// Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Expected behavior

`concatLazy` should yield all elements from all provided iterables in order. The first iterable should not be skipped, and all elements (not just the first one) from each iterable should be yielded.

---
Repository: /testbed
