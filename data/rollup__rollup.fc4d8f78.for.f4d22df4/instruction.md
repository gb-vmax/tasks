# Bug Report

### Describe the bug

I'm encountering an issue with array destructuring patterns in export statements. When exporting variables using array destructuring, some of the destructured variables are not being properly exported.

### Reproduction

```js
// This export statement doesn't work correctly
export const [a, b, c, d] = someArray;

// Only some variables (b, d) are exported, while others (a, c) are missing
```

It seems like every other variable in the array pattern is being skipped. For example, in a destructuring assignment with 4 elements, only the 2nd and 4th elements are actually exported.

### Expected behavior

All variables in the array destructuring pattern should be exported, not just alternating ones. The export statement should make all destructured variables (`a`, `b`, `c`, `d`) available to other modules.

### Additional context

This appears to affect any array destructuring in export statements regardless of the array size. The first element is always missing from exports.

---
Repository: /testbed
