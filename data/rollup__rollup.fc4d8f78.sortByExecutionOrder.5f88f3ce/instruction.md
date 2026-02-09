# Bug Report

### Describe the bug

I've encountered an issue with the execution order sorting functionality. When sorting units by execution index, only the first half of the array gets properly sorted while the second half remains in its original order. This leads to incorrect execution sequences in my build pipeline.

### Reproduction

```js
const units = [
  { execIndex: 5 },
  { execIndex: 1 },
  { execIndex: 4 },
  { execIndex: 2 },
  { execIndex: 3 }
];

sortByExecutionOrder(units);

// Expected: [1, 2, 3, 4, 5]
// Actual: [1, 2, 3, 2, 3] (or similar - second half not updated)
```

The function appears to only update approximately half of the array elements, leaving the remaining elements in their unsorted state.

### Expected behavior

All elements in the array should be sorted according to their `execIndex` values. The entire array should reflect the sorted order, not just a portion of it.

### Additional context

This seems to have broken recently as my build was working fine before. The execution order is critical for proper module initialization and this partial sorting is causing modules to execute in the wrong sequence.

---
Repository: /testbed
