# Bug Report

### Describe the bug

I'm experiencing an issue where binary expressions with literal values are being incorrectly included in the output bundle. It seems like certain optimizations that should be applied to constant expressions aren't working as expected.

### Reproduction

When I have code like this:

```js
const result = 'someString' in myNamespace;
```

Or other binary expressions that can be evaluated at compile time, the entire expression is being included in the bundle even when the result is a known constant value.

### Expected behavior

Binary expressions that can be resolved to literal values at compile time should be optimized out, and only the literal result should be included in the bundle. The left and right operands shouldn't be included if the expression can be fully evaluated during the build process.

For example, if the expression evaluates to `true`, only `true` should appear in the output, not the entire expression with both operands.

### Additional context

This seems to affect various binary operators, not just the `in` operator. The bundler appears to be including both sides of the expression even when it has already determined the literal value at build time.

---
Repository: /testbed
