# Bug Report

### Describe the bug

Sorting numbers in descending order is not working correctly. When I try to sort an array of numbers in descending order, they end up in ascending order instead.

### Reproduction

```js
const numbers = [5, 2, 8, 1, 9];
const sorted = numbers.sort(descendingNumberSort);

// Expected: [9, 8, 5, 2, 1]
// Actual: [1, 2, 5, 8, 9]
```

The `descendingNumberSort` function appears to be sorting in ascending order rather than descending. This is breaking any feature that relies on descending numeric sorting.

### Expected behavior

Numbers should be sorted from highest to lowest when using `descendingNumberSort`.

---
Repository: /testbed
