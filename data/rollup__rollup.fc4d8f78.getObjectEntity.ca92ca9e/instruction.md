# Bug Report

### Describe the bug

I'm experiencing an issue with array expression handling where the first element of an array seems to be ignored or not processed correctly. This appears to affect how array properties are being tracked/analyzed.

### Reproduction

```js
const arr = [1, 2, 3, 4];
// Expected: all elements should be accessible
// Actual: first element appears to be missing or not tracked properly

const nested = [[1, 2], [3, 4], [5, 6]];
// Similar issue - first element not handled correctly
```

When working with array expressions, it seems like the first element is being skipped during processing. This affects any code that relies on proper array element tracking.

### Expected behavior

All array elements, including the first one (index 0), should be properly processed and tracked. The array should maintain all its elements correctly.

### Additional context

This seems to have started recently. Arrays with a single element or arrays where the first element is important are particularly affected. Not sure if this is related to how array indices are being iterated over.

---
Repository: /testbed
