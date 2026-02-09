# Bug Report

### Describe the bug

I'm experiencing an issue with binary expressions in my code where certain operations are not being included in the output bundle correctly. It seems like when using binary expressions that can be evaluated at compile-time, the left and right operands are sometimes missing from the final output.

### Reproduction

```js
// This code doesn't work as expected
const obj = { foo: 'bar' };
const result = 'foo' in obj;
```

When bundling code that contains the `in` operator with object literals, the expression gets optimized away but the operands are not properly included in the output. The bundle is missing necessary code.

### Expected behavior

Both sides of binary expressions should be included in the bundle even when the expression can be evaluated to a literal value at compile-time. The `in` operator should work correctly and all necessary code should be present in the output.

### Additional context

This appears to affect the `in` operator specifically. Other binary operators seem to work fine. The issue manifests when the expression could theoretically be evaluated statically but the operands still need to be in the output for runtime evaluation.

---
Repository: /testbed
