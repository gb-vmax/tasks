# Bug Report

### Describe the bug

When using prefix update expressions (like `++x` or `--x`) in the SystemJS output format with exported variables, the generated code is incorrect. The operator being used in the export sequence is wrong - it's using the second character of the operator string instead of the first character.

### Reproduction

```js
// Input code
export let counter = 0;

function increment() {
  ++counter;
}

// When bundled with format: 'system'
// The generated code uses the wrong operator in the export update
```

For update expressions like `++` or `--`, the code is extracting `operator[1]` (which would be the second `+` or `-`) instead of `operator[0]` (the first character), causing the export synchronization to use an incorrect operator.

### Expected behavior

Prefix update expressions on exported variables should correctly use the first character of the operator (`+` or `-`) when generating the SystemJS export sequence, not the second character.

### System Info
- Rollup version: latest
- Output format: system
- Node version: any

---
Repository: /testbed
