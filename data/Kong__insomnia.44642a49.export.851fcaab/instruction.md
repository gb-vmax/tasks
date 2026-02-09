# Bug Report

### Describe the bug

I'm experiencing an issue with the `descendingNumberSort` function - it's sorting numbers in ascending order instead of descending order. When I try to sort a list of numbers in descending order, they end up being sorted in ascending order instead.

### Reproduction

```js
const numbers = [5, 2, 8, 1, 9];
const sorted = numbers.sort(descendingNumberSort);

// Expected: [9, 8, 5, 2, 1]
// Actual: [1, 2, 5, 8, 9]
```

The function appears to be doing the opposite of what it should - it's sorting in ascending order when it should be sorting in descending order.

### Expected behavior

When using `descendingNumberSort`, numbers should be sorted from highest to lowest (descending order), not lowest to highest.

### System Info
- Version: latest
- OS: macOS

---
Repository: /testbed
