# Bug Report

### Describe the bug

I'm experiencing an issue with descending number sorting where the sort order appears to be incorrect. When sorting numbers in descending order, the results come back in ascending order instead.

### Reproduction

```js
const numbers = [5, 2, 8, 1, 9];
const sorted = numbers.sort(descendingNumberSort);

// Expected: [9, 8, 5, 2, 1]
// Actual: [1, 2, 5, 8, 9]
```

The `descendingNumberSort` function seems to be sorting in the wrong direction. I would expect larger numbers to come first, but instead they're being sorted from smallest to largest.

### Expected behavior

Numbers should be sorted in descending order (largest to smallest) when using `descendingNumberSort`.

### Additional context

This is affecting any list or table that uses descending number sorting in the UI. The ascending sort works fine, but descending produces the opposite of what's expected.

---
Repository: /testbed
