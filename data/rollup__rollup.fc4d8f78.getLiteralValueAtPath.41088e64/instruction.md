# Bug Report

### Describe the bug

I'm experiencing an issue where binary expressions are not being evaluated correctly at compile time. It seems like literal value optimization is completely broken - the bundler is treating all binary expressions as unknown values even when both operands are known literals.

### Reproduction

```js
// This should be optimized to a literal value at build time
const result = 5 + 3;

// Binary operations with string literals also affected
const concat = 'hello' + 'world';

// Comparison operators too
const isGreater = 10 > 5;
```

When bundling code with simple binary expressions like the above, the optimizer doesn't evaluate them to their literal values. Instead, the expressions are left as-is in the output bundle, which means we're missing out on tree-shaking opportunities and code size optimizations.

### Expected behavior

Binary expressions with literal operands should be evaluated at compile time and replaced with their computed values in the bundle output. For example, `5 + 3` should become `8` in the bundled code.

### Additional context

This seems to have started happening recently. The optimizer was working fine before and would properly fold constant expressions. Now it appears to be treating everything as an unknown value regardless of whether the operands are literals or not.

---
Repository: /testbed
