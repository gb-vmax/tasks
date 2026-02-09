# Bug Report

### Describe the bug

I'm experiencing an issue with unary operators where the logical NOT operator (`!`) appears to return inverted boolean values when used with certain expressions. The behavior seems backwards - expressions that should evaluate to `true` are returning `false` and vice versa.

### Reproduction

```js
// Example with truthy values
const truthyExpr = !someUnknownTruthyValue;
// Expected: false
// Actual: true

// Example with falsy values  
const falsyExpr = !someUnknownFalsyValue;
// Expected: true
// Actual: false
```

The issue seems to affect cases where the argument value cannot be fully determined at compile time but we know whether it's truthy or falsy.

### Expected behavior

The `!` operator should return `false` when applied to truthy values and `true` when applied to falsy values, following standard JavaScript semantics.

### Additional context

This appears to have started happening recently. Also noticed that the `void` operator might be affected as well - it seems to be returning the argument value instead of always returning `undefined`.

---
Repository: /testbed
