# Bug Report

### Describe the bug

I'm experiencing incorrect behavior with logical expressions (`&&` and `||`) when rollup tries to evaluate them. It seems like the operators are being treated in reverse - `||` is behaving like `&&` and vice versa.

### Reproduction

```js
// Example 1: OR operator returning wrong value
const result1 = false || "fallback";
// Expected: "fallback" (truthy)
// Getting: treated as falsy

// Example 2: AND operator returning wrong value  
const result2 = true && "value";
// Expected: "value" (truthy)
// Getting: treated as falsy
```

When bundling code with these logical expressions, the output seems to optimize them incorrectly. The `||` operator appears to be returning falsy values when it should return truthy ones, and the `&&` operator is doing the opposite.

### Expected behavior

- `false || "fallback"` should be treated as truthy (returns "fallback")
- `true && "value"` should be treated as truthy (returns "value")
- `false && anything` should be treated as falsy
- `true || anything` should be treated as truthy

The logical operators should follow standard JavaScript semantics where:
- `||` returns the first truthy value or the last value
- `&&` returns the first falsy value or the last value

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
