# Bug Report

### Describe the bug

I'm experiencing an issue with SystemJS output format where exported variables are being referenced before they're actually exported. This causes runtime errors when the code executes because the export statement comes after the variable reference in the generated sequence.

### Reproduction

When using SystemJS format with exported variable sequences, the generated code produces something like:

```js
expression, variableName, System.register(...)
```

But this means `variableName` is accessed before the export is registered with SystemJS, which can lead to undefined references or incorrect module initialization order.

### Expected behavior

The export statement should come before the variable reference in the sequence:

```js
expression, System.register(...), variableName
```

This way the variable is properly exported to the SystemJS registry before being referenced.

### Additional context

Also noticed that when parentheses are needed around the expression, they seem to be added in the wrong direction (prependRight instead of appendLeft and vice versa), which could cause malformed output.

This appears to affect the order of operations in the generated SystemJS module code.

---
Repository: /testbed
