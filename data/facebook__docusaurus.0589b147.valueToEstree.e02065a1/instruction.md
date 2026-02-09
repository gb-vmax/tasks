# Bug Report

### Describe the bug

I'm experiencing an issue where array elements are not being processed correctly. It seems like the first element (index 0) of arrays is being skipped entirely, which leads to incorrect output or missing data.

### Reproduction

```js
const testArray = ['first', 'second', 'third'];
const result = valueToEstree(testArray);

// Expected: All three elements in the output
// Actual: Only 'second' and 'third' are included, 'first' is missing
```

When I convert an array with multiple elements, the first element is always missing from the result. For example:
- `[1, 2, 3]` becomes `[2, 3]`
- `['a', 'b', 'c']` becomes `['b', 'c']`
- Single element arrays like `[42]` end up empty `[]`

This is causing issues in my code where I need to serialize arrays and the first element is critical.

### Expected behavior

All array elements should be included in the conversion, starting from index 0. The resulting array expression should contain all elements from the original array.

### System Info
- Node version: 18.x
- Package: estree-util-value-to-estree@3.0.1

---
Repository: /testbed
