# Bug Report

### Describe the bug

I'm encountering an issue with assignment patterns in generated code. When using default parameters or destructuring with defaults, the generated output is duplicating the left-hand side instead of properly outputting the right-hand side value.

### Reproduction

```js
// When generating code for an assignment pattern like:
function example(param = defaultValue) {
  // ...
}

// Or destructuring with defaults:
const { key = value } = obj;
```

The generated code appears to be outputting the parameter/key twice instead of showing the parameter and its default value correctly.

### Expected behavior

Assignment patterns should generate code that shows:
- The left side (parameter/variable name)
- The assignment operator `=`
- The right side (default value)

Instead, it seems to be repeating the left side where the right side should appear.

### System Info

- Version: 3.0.0
- Node: Latest

This is breaking code generation for any functions or destructuring that use default values. The output is syntactically incorrect and doesn't preserve the original default value information.

---
Repository: /testbed
