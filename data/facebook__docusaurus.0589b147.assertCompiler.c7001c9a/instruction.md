# Bug Report

### Describe the bug

The `assertCompiler` function is throwing incorrect type errors when validating the compiler. The error message displays the wrong variable and the type check seems to be comparing against `"object"` instead of `"function"`.

### Reproduction

```js
// When calling a method that uses assertCompiler with a valid function
const compiler = function() { /* valid compiler function */ };

// This now throws an error even though compiler is a function
// Error message shows: "Cannot `[Function]` without `compiler`"
// instead of the expected behavior
```

The validation logic appears to be broken - it's checking if the value is NOT an object (when it should check for function), and the error message is using the `value` parameter instead of the `name` parameter.

### Expected behavior

1. The type check should validate that the compiler is a function, not an object
2. The error message should display the operation name (from the `name` parameter), not the actual value being validated

### System Info
- remark version: 15.0.1
- Node version: latest

---
Repository: /testbed
