# Bug Report

### Describe the bug

When using SystemJS output format with export statements, the generated code produces incorrect variable names in the IIFE wrapper. The exported value is not properly returned because the parameter name doesn't match the variable being used in the return statement.

### Reproduction

```js
// Input code with export
export default someFunction();

// Generated SystemJS output has mismatched variables
// The IIFE receives 'exports' as parameter but tries to return 'v'
// causing the export to be undefined
```

### Expected behavior

The generated SystemJS code should use consistent variable names in the IIFE wrapper so that the exported value is properly returned and accessible to the module system.

### System Info
- Rollup version: latest
- Output format: systemjs
- Node version: 18.x

This seems to have broken after a recent change. The export statement generates code but the actual value being exported comes out as undefined when the module is loaded.

---
Repository: /testbed
