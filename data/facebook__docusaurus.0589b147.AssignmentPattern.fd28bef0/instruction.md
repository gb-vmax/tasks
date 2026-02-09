# Bug Report

### Describe the bug

I'm experiencing an issue with destructuring assignment patterns where the default value and the variable name appear to be swapped in the generated output. When using parameter defaults in function declarations, the output code has the assignment backwards.

### Reproduction

```js
// Input code with default parameter
function example(param = defaultValue) {
  // ...
}

// Expected output should be:
// param = defaultValue

// But getting:
// defaultValue = param
```

This affects any code using assignment patterns with defaults, including:
- Function parameter defaults
- Destructuring with default values
- Arrow function parameters with defaults

### Expected behavior

The generated code should maintain the correct order where the parameter/variable name comes first, followed by the equals sign, then the default value. Currently it's reversed which produces invalid JavaScript.

### System Info
- MDX version: 3.0.0
- Node version: Latest

---
Repository: /testbed
