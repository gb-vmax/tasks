# Bug Report

### Logical expression evaluation issue with nullish coalescing operator

I'm encountering unexpected behavior with the nullish coalescing operator (`??`) when evaluating expressions. The operator seems to be treating `undefined` incorrectly.

### Reproduction

```js
const value = undefined;
const result = value ?? 'default';
// Expected: 'default'
// Actual behavior: incorrect evaluation
```

The issue appears when the left-hand side of a `??` expression is `undefined`. According to the spec, the nullish coalescing operator should return the right-hand side when the left is either `null` or `undefined`, but it seems to only handle `null` correctly.

### Expected behavior

When using `??`, both `null` and `undefined` values on the left side should cause the right side to be evaluated and returned. Currently it seems like only `null` is being handled properly.

### Additional context

This is affecting tree-shaking and code optimization in my bundle. The bundler isn't correctly identifying which branch will be used at runtime when `undefined` values are involved.

---
Repository: /testbed
