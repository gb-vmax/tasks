# Bug Report

### Describe the bug

When using SystemJS output format with exported variables in expressions, the generated code has incorrect syntax. The parentheses for wrapping expressions are placed in the wrong positions, and there's an issue with comma placement in the export sequence.

### Reproduction

```js
// Input code with an exported variable in an expression
export let x;
x = someExpression();

// Expected output (SystemJS format):
// (System.register(...), x = someExpression(), System.export('x', x), x)

// Actual output has malformed syntax with misplaced parentheses and commas
```

### Expected behavior

The SystemJS export sequence should generate valid JavaScript with:
- Properly placed opening and closing parentheses around the entire expression when needed
- Correct comma placement between the export statement and variable reference

### System Info
- Rollup version: latest
- Output format: systemjs
- Node version: 18.x

---
Repository: /testbed
