# Bug Report

### Describe the bug
The `descendingNumberSort` function is not sorting numbers in descending order correctly. When I use it to sort an array of numbers, the results are inconsistent and don't match what I'd expect from a descending sort.

### Reproduction
```js
const numbers = [1, 5, 3, 9, 2];
const sorted = numbers.sort(descendingNumberSort);

// Expected: [9, 5, 3, 2, 1]
// Getting unexpected order
```

I noticed this when trying to sort a list of response times in the UI - they're appearing in the wrong order. The ascending sort works fine, but descending is definitely broken.

### Expected behavior
Numbers should be sorted from highest to lowest when using `descendingNumberSort`.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
