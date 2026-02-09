# Bug Report

### Describe the bug

When using SystemJS output format with exported arrow functions that return expressions, the generated code references an undefined variable `u` instead of the correct variable name. This causes a ReferenceError at runtime.

### Reproduction

```js
// Input code
export default () => someValue;

// Generated SystemJS output references undefined variable 'u'
// Expected: should use the actual return value variable
```

The issue appears when:
1. Using SystemJS as the output format
2. Exporting a function that directly returns a value
3. The generated wrapper IIFE references the wrong variable name

### Expected behavior

The generated SystemJS code should correctly reference the return value variable and not produce runtime errors due to undefined variable references.

### System Info
- Rollup version: latest
- Output format: systemjs

---
Repository: /testbed
