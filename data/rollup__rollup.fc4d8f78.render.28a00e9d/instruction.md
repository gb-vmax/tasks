# Bug Report

### Describe the bug

When using the `system` format with update expressions (like `++` or `--`), the generated code for exported variables is incorrect. Specifically, when a prefix update expression is used in a non-expression statement context with multiple export names, the output seems to be malformed.

### Reproduction

```js
// input.js
export let counter = 0;

function increment() {
  ++counter;
}

export { counter as aliasedCounter };
```

Build with `system` format and the generated code for the prefix increment operation doesn't work as expected when the variable has multiple exports.

### Expected behavior

The system format should correctly handle prefix update expressions (`++variable`, `--variable`) on exported variables, even when those variables are exported under multiple names. The generated code should properly update the variable and notify all exports.

### Additional context

This appears to affect scenarios where:
- Using `system` output format
- Variable is exported with multiple names (e.g., default export + named export, or multiple aliases)
- Using prefix update operators (`++` or `--`)

The postfix versions (e.g., `counter++`) seem to work fine, it's specifically the prefix operators that have issues.

---
Repository: /testbed
