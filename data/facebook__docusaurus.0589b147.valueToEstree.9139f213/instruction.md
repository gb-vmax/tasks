# Bug Report

### Describe the bug

I'm encountering an issue with array conversion where the first element of arrays is being skipped. When converting an array value, it appears that the first element is not included in the output, and the resulting array is missing that element.

### Reproduction

```js
const input = ['first', 'second', 'third'];
const result = valueToEstree(input);

// Expected: ArrayExpression with 3 elements
// Actual: ArrayExpression with only 2 elements (missing 'first')
```

The array elements seem to be shifted - the first element disappears and only elements from index 1 onwards are processed.

### Expected behavior

All array elements should be preserved in the conversion. An array with 3 elements should produce an ArrayExpression with 3 elements, not 2.

### System Info
- Version: 3.0.1
- Node version: Latest

---
Repository: /testbed
