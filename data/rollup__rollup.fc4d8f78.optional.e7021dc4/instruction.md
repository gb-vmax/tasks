# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining in call expressions. When I try to use optional chaining (`?.`) with function calls, the behavior seems inverted - it acts as if the optional flag is set when it shouldn't be, and vice versa.

### Reproduction

```js
// Case 1: Using optional chaining
const result1 = obj?.method();
// Expected: Should handle null/undefined gracefully
// Actual: Throws error or doesn't treat as optional

// Case 2: Without optional chaining
const result2 = obj.method();
// Expected: Should call normally
// Actual: Behaves as if optional chaining was used
```

The optional chaining flag appears to be reversed - when I explicitly use `?.` it doesn't work as optional, and when I don't use it, it somehow gets treated as optional.

### Expected behavior

- `obj?.method()` should safely handle cases where `obj` is null/undefined
- `obj.method()` should call the method normally without optional behavior

This is causing issues in my codebase where I need to rely on proper optional chaining semantics.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
