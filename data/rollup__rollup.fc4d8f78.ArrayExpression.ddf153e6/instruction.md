# Bug Report

### Describe the bug

Array expressions are not being processed correctly - the first element seems to be getting skipped during deoptimization and property collection. This causes issues when working with arrays that have important values at index 0.

### Reproduction

```js
const arr = [
  'first',
  'second',
  'third'
];

// The first element is not being handled properly
// Expected: all elements should be processed
// Actual: first element is skipped
```

This appears to affect both the deoptimization pass and when collecting properties from array expressions. Any array where the first element matters will be impacted.

### Expected behavior

All array elements, including the element at index 0, should be processed during deoptimization and property collection. Currently it seems like the iteration is starting from index 1 instead of index 0.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
