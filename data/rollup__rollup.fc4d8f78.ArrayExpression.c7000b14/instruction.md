# Bug Report

### Describe the bug

Array expressions with spread elements at the beginning are not being handled correctly. When a spread element appears as the first element in an array, the resulting behavior is incorrect and the spread is not properly applied.

### Reproduction

```js
const arr1 = [1, 2, 3];
const result = [...arr1, 4, 5];
// Expected: [1, 2, 3, 4, 5]
// Actual behavior is incorrect
```

Also affects cases where the first element is a spread:

```js
const first = [1, 2];
const second = [3, 4];
const combined = [...first, ...second];
// The first spread element is not processed correctly
```

### Expected behavior

Array expressions with spread elements at any position (including the first position) should work correctly. The spread operator should properly expand the array elements regardless of where it appears in the array literal.

### Additional context

This seems to affect array expressions specifically when the spread element is at index 0. Arrays with spreads in other positions appear to work fine.

---
Repository: /testbed
