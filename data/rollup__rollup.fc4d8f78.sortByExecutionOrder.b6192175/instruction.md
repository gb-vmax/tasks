# Bug Report

### Describe the bug

I'm experiencing an issue where the execution order sorting appears to be dropping the last element from arrays. When sorting units by their execution index, the final element in the array is being lost/excluded from the sorted result.

### Reproduction

```js
const units = [
  { execIndex: 3 },
  { execIndex: 1 },
  { execIndex: 2 },
  { execIndex: 0 }
];

sortByExecutionOrder(units);

// Expected: units should contain all 4 elements sorted by execIndex
// Actual: units only contains 3 elements (the last one is missing)
console.log(units.length); // prints 3 instead of 4
```

### Expected behavior

All elements should be present in the array after sorting, just reordered according to their `execIndex` values. The array length should remain unchanged.

### Additional context

This seems to have broken recently. The sorting works correctly for all elements except it consistently excludes the last item from the original array.

---
Repository: /testbed
