# Bug Report

### Describe the bug

I'm encountering an issue where binary expressions are not being evaluated correctly. It seems like literal value optimization has completely broken - the compiler is always returning `UnknownValue` even for simple expressions that should be statically analyzable.

### Reproduction

```js
// Simple binary expression that should be optimizable
const result = 5 + 3;

// This should be able to determine the literal value at compile time
// but it's being treated as UnknownValue
```

Also seeing issues with the `in` operator optimization for namespace exports. The compiler used to optimize expressions like `'export' in namespace`, but now it's not working as expected.

### Expected behavior

The compiler should be able to determine literal values for binary expressions when both operands are known at compile time. This is important for tree-shaking and dead code elimination.

Additionally, namespace export checking with the `in` operator should be optimized properly.

### Additional context

This seems to have started happening recently. The optimization for detecting runtime type coercion errors with the `+` operator also appears to be inverted - it's now triggering on operators that are NOT `+` instead of when the operator IS `+`.

---
Repository: /testbed
