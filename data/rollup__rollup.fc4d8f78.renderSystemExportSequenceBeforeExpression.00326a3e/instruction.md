# Bug Report

### Describe the bug

When using SystemJS output format with exported variables that require parentheses wrapping, the generated code has incorrect syntax. The closing parenthesis appears in the wrong position, causing the export statement to be malformed.

### Reproduction

```js
// Given a module with an expression that needs parentheses
export const foo = someCondition ? value1 : value2;

// The generated SystemJS code places the closing paren incorrectly
// Expected: System.register([], function (_export) { ... _export("foo", (someCondition ? value1 : value2)), ... })
// Actual: The parenthesis positioning is wrong, breaking the syntax
```

This seems to affect conditional expressions and other cases where the exported expression needs to be wrapped in parentheses for the SystemJS format.

### Expected behavior

The SystemJS export statement should have properly balanced parentheses around the expression, with the closing paren appearing after the expression ends, not at the start position.

### System Info
- Rollup version: latest
- Output format: systemjs

---
Repository: /testbed
