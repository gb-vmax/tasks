# Bug Report

### Describe the bug

I'm getting incorrect literal values when using sequence expressions in my code. It seems like the wrong expression in the sequence is being evaluated to get the literal value.

### Reproduction

```js
const result = (1, 2, 3);
console.log(result); // Should be 3, but getting 1 instead
```

When I have a sequence expression like `(expr1, expr2, expr3)`, the literal value being returned is from the first expression instead of the last one. According to JavaScript semantics, a sequence expression should evaluate to the value of its last expression, not the first.

This is affecting my bundled code where I'm using comma operators for side effects followed by a return value.

### Expected behavior

Sequence expressions should return the value of the last expression in the sequence, not the first one. For example:
- `(1, 2, 3)` should evaluate to `3`
- `(foo(), bar(), 42)` should evaluate to `42`

Currently it appears to be returning the first value instead.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
