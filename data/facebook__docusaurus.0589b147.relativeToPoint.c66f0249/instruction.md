# Bug Report

### Describe the bug

I'm experiencing an issue with position mapping in MDX where certain boundary conditions are being handled incorrectly. When the relative position exactly matches a stop point, the mapping returns the wrong index.

### Reproduction

```js
// When stops array has positions like [0, 10, 20, 30]
// and we query for position 10 (which exactly matches a stop)
const stops = [[0, ...], [10, ...], [20, ...], [30, ...]];
const result = relativeToPoint(stops, 10);

// Expected: should return index 1 (the stop at position 10)
// Actual: returns index 2 (the stop AFTER position 10)
```

This causes off-by-one errors when mapping positions that fall exactly on stop boundaries. The issue appears to be in the `relativeToPoint` function where it's using the wrong comparison operator for the boundary check.

### Expected behavior

When a relative position exactly matches a stop point, it should return that stop's index, not the next one.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
