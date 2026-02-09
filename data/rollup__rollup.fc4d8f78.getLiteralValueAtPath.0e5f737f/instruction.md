# Bug Report

### Describe the bug

I'm experiencing incorrect behavior with logical expressions (`&&` and `||`) when evaluating literal values. The operators seem to be returning the wrong unknown value types based on the boolean evaluation of the right-hand side.

### Reproduction

```js
// For && operator with truthy right value
const expr1 = someValue && true;
// Expected: Should return UnknownTruthyValue when right is truthy
// Actual: Returns UnknownFalsyValue

// For || operator with falsy right value  
const expr2 = someValue || false;
// Expected: Should return UnknownFalsyValue when right is falsy
// Actual: Returns UnknownTruthyValue
```

The logic appears to be inverted - when the right side of `&&` evaluates to truthy, it's returning a falsy unknown value, and when the right side of `||` evaluates to falsy, it's returning a truthy unknown value.

### Expected behavior

- For `&&` operator: When right value is truthy, should return `UnknownTruthyValue`
- For `&&` operator: When right value is falsy, should return `UnknownFalsyValue`
- For `||` operator: When right value is truthy, should return `UnknownTruthyValue`  
- For `||` operator: When right value is falsy, should return `UnknownFalsyValue`

This is affecting tree-shaking and optimization decisions in my builds.

---
Repository: /testbed
