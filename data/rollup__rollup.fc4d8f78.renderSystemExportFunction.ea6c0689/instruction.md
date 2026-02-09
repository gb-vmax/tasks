# Bug Report

### Describe the bug

I'm experiencing an issue with SystemJS export rendering where variable names are being shadowed incorrectly. When exporting a value from a function expression, the generated code uses a variable name that conflicts with the actual exported value, causing the wrong value to be returned.

### Reproduction

```js
// Input code with a function expression that returns a value
export default function() {
  return someValue;
}();

// The generated SystemJS output incorrectly references the variable
// Expected: the function's return value should be exported
// Actual: the wrapper variable shadows the actual value
```

When the code is transpiled to SystemJS format, the IIFE wrapper introduces a variable that conflicts with the value being exported, resulting in the exported value being incorrect.

### Expected behavior

The generated SystemJS code should properly export the return value of the function expression without variable name conflicts. The wrapper variable should use a name that doesn't shadow the actual exported value.

### System Info
- Rollup version: latest
- Module format: SystemJS

---
Repository: /testbed
