# Bug Report

### Describe the bug

I'm experiencing an issue with SystemJS output format where exported expressions are being wrapped incorrectly with parentheses. The parentheses appear to be in the wrong positions, causing invalid JavaScript syntax to be generated.

### Reproduction

When using SystemJS format with an export that requires parentheses wrapping (like certain expression sequences), the generated code has misplaced parentheses.

Example configuration:
```js
{
  format: 'system',
  // export a variable that needs expression sequence handling
}
```

The generated SystemJS output has the opening and closing parentheses reversed in position, resulting in malformed code that won't execute properly.

### Expected behavior

The parentheses should wrap the expression correctly, with `(` before the expression and `)` after it, not the other way around. The system export statement should also be placed at the correct position relative to the expression.

### System Info
- Rollup version: latest
- Output format: system
- Node version: 18.x

---
Repository: /testbed
