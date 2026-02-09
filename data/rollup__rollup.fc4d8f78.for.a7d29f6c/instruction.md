# Bug Report

### Describe the bug

I'm experiencing an issue with the `concatLazy` iterator utility function. When concatenating multiple iterables, the first element from each iterable is being skipped/missing from the output. This is causing data loss in my application where I'm using this function to merge multiple data streams.

### Reproduction

```js
const iter1 = [1, 2, 3];
const iter2 = [4, 5, 6];
const iter3 = [7, 8, 9];

const result = Array.from(concatLazy([iter1, iter2, iter3]));
console.log(result);
// Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
// Actual: [2, 3, 5, 6, 8, 9] (missing 1, 4, 7)
```

### Expected behavior

All elements from all iterables should be yielded in order. The concatenated result should contain every element from the input iterables without skipping any values.

### Additional context

This appears to have started happening recently. I'm using this utility to combine multiple data sources and the missing first elements are causing issues downstream in my data processing pipeline.

---
Repository: /testbed
