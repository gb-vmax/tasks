# Bug Report

### Describe the bug

When declaring multiple variables in a single statement, the last variable in the declaration is not being properly initialized. This affects variable declarations with multiple declarators like `const a = 1, b = 2, c = 3` where the final variable (`c` in this example) doesn't get processed correctly.

### Reproduction

```js
// Multiple variable declarations in one statement
const x = 1, y = 2, z = 3;

// Expected: all three variables (x, y, z) should be properly declared
// Actual: only x and y are handled correctly, z is not initialized properly
```

This also affects destructuring patterns:

```js
const { a, b } = obj1, { c, d } = obj2;
// Only the first destructuring works as expected
```

### Expected behavior

All variables in a multi-variable declaration statement should be initialized and declared properly, regardless of their position in the declaration list.

### Additional context

This seems to be a regression - it was working fine in previous versions. The issue only manifests when there are 2 or more variables declared in the same statement.

---
Repository: /testbed
