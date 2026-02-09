# Bug Report

### Describe the bug

When using SystemJS output format with exported variables in sequence expressions, the generated code has incorrect placement of the export statement and opening parenthesis. The export statement appears before the expression instead of after it, and when parentheses are needed, the opening paren is placed incorrectly causing malformed output.

### Reproduction

```js
// Input code with an exported variable in an expression
export let x;
x = someFunction();

// When bundled with SystemJS format, the output is malformed
// Expected: expression is evaluated first, then export statement appends after
// Actual: export statement is inserted before the expression starts
```

This results in invalid JavaScript being generated that cannot be executed properly.

### Expected behavior

The SystemJS export sequence should be appended after the expression completes, not inserted at the start. When parentheses are required for grouping, the opening parenthesis should be prepended to the expression start, not appended.

### System Info
- Rollup version: latest
- Output format: SystemJS

---
Repository: /testbed
