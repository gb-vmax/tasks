# Bug Report

### Describe the bug

I'm experiencing an issue with `for...in` loops where the loop variable seems to be getting assigned before proper initialization. This causes unexpected behavior when the left-hand side of the loop contains complex destructuring patterns or variable declarations.

### Reproduction

```js
for (const key in obj) {
  // Loop variable 'key' behaves unexpectedly
  console.log(key);
}
```

When using `for...in` statements with variable declarations, the assignment seems to happen in the wrong order during the initialization phase, which can lead to incorrect behavior in the generated output.

### Expected behavior

The loop variable should be properly initialized before any assignment operations occur. The initialization order should ensure that the parent class initialization happens first, followed by any variable assignments.

### Additional context

This appears to be related to how the AST node handles initialization of the left-hand side expression in `for...in` loops. The timing of when values are assigned to the loop variable seems off.

---
Repository: /testbed
