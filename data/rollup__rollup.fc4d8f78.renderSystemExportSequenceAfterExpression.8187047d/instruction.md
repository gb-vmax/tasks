# Bug Report

### Describe the bug

When using SystemJS output format with exported variables that need parentheses wrapping, the generated code has incorrect placement of the export statement and parentheses. The export sequence appears before the expression instead of after it, and the parentheses are in the wrong positions.

### Reproduction

```js
// Input code with an expression that exports a variable
export const result = someFunction();

// Expected output (SystemJS format):
// (expression, exports('result', result), result)

// Actual output:
// (exports('result', result), result, expression)
```

The export statement and variable reference are being inserted at the start of the expression instead of after it, which breaks the expected evaluation order.

### Expected behavior

The SystemJS export sequence should be appended after the expression, not prepended before it. The opening parenthesis should come before the expression starts, and the closing parenthesis should come after the expression ends.

### System Info
- Rollup version: latest
- Output format: systemjs

---
Repository: /testbed
