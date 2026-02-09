# Bug Report

### Describe the bug

Logical expressions with `||` and `&&` operators are not being optimized correctly. When using these operators, the bundler seems to be producing incorrect output for certain edge cases involving falsy and truthy values.

### Reproduction

```js
// Case 1: OR operator with falsy right side
const result1 = someCondition || false;
// Expected: should recognize false as falsy
// Actual: not optimized correctly

// Case 2: AND operator with truthy right side  
const result2 = someCondition && true;
// Expected: should recognize true as truthy
// Actual: not optimized correctly
```

The issue appears when the bundler tries to determine literal values for logical expressions. It's treating `||` expressions with falsy right-hand values and `&&` expressions with truthy right-hand values incorrectly.

### Expected behavior

The bundler should correctly identify and optimize:
- `||` expressions where the right side evaluates to a falsy value
- `&&` expressions where the right side evaluates to a truthy value

This affects tree-shaking and dead code elimination in the final bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
