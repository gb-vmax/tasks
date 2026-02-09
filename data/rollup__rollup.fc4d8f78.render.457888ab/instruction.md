# Bug Report

### Describe the bug

When using prefix update expressions (like `++x`) with exported variables in SystemJS format, the export handling appears to be inverted. Variables with a single export name are being handled with the sequence logic, while variables with multiple export names are using the simple expression logic. This causes incorrect code generation for SystemJS module exports.

### Reproduction

```js
// Input module with exported variable
export let counter = 0;

function increment() {
  ++counter; // prefix increment
}

// When bundled with format: 'system', the generated code
// for the prefix increment doesn't properly update exports
```

For a variable with a single export name, the prefix increment should generate simple export update code, but instead it's generating the more complex sequence expression pattern.

### Expected behavior

Prefix update expressions on exported variables should:
- Use `renderSystemExportExpression` when there's exactly ONE export name
- Use `renderSystemExportSequenceAfterExpression` when there are MULTIPLE export names

Currently this logic appears to be backwards.

### Additional context

This only affects the SystemJS output format when using prefix update operators (`++x`, `--x`) on exported variables. Postfix operators (`x++`, `x--`) may also be affected in expression statement contexts.

---
Repository: /testbed
