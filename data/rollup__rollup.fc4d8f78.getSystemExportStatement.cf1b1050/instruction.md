# Bug Report

### Describe the bug

When generating SystemJS export statements, the output format is incorrect when there are multiple exports or when modifiers are involved. The export names and variable names appear to be swapped or placed in the wrong positions in the generated code.

### Reproduction

When bundling code with SystemJS output format that has:
1. Multiple export names for the same variable
2. Export statements with modifiers

The generated `exports()` call has incorrect parameter ordering. For example:

```js
// Expected output format:
exports('myExport', myVariable)

// But getting something like:
exports('myExportmodifier', myVariable) // modifier in wrong place
```

Or when there's a single export with multiple names, it seems to pick the wrong export name from the list instead of the first one.

### Expected behavior

The SystemJS export statements should have:
- Correct export name as the first parameter
- Correct variable name as the second parameter  
- Modifiers applied to the variable name, not the export name

### System Info
- Rollup version: latest
- Output format: SystemJS

---
Repository: /testbed
