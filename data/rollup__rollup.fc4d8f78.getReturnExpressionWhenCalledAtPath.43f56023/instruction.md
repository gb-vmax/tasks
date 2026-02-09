# Bug Report

### Describe the bug

I'm experiencing an issue with boolean literal method calls in my code. When I try to call methods on boolean values (like `.toString()` or `.valueOf()`), the behavior seems incorrect and doesn't match what I'd expect from standard JavaScript.

### Reproduction

```js
const result = true.toString();
// Expected: "true"
// Actual: unexpected behavior or error

const boolValue = false.valueOf();
// Expected: false
// Actual: unexpected behavior
```

This seems to affect any method calls on boolean literals. The issue appears when the code tries to determine the return type of these method invocations.

### Expected behavior

Boolean literal methods should work the same way they do in standard JavaScript:
- `true.toString()` should return the string `"true"`
- `false.valueOf()` should return the boolean `false`
- Other boolean prototype methods should behave correctly

### Additional context

This might be related to how the AST handles member expressions on boolean literals. It worked fine in previous versions but seems to have broken recently.

---
Repository: /testbed
