# Bug Report

### Describe the bug

Global variables are not being treated as reassignable, causing incorrect tree-shaking and bundling behavior. When a global variable is referenced in the code, the bundler doesn't account for the possibility that it might be reassigned elsewhere, leading to incorrect optimization assumptions.

### Reproduction

```js
// input.js
export function checkGlobal() {
  return globalVar;
}

// The bundler should assume globalVar could be reassigned
// but it's being treated as a constant binding
```

When bundling this code, the global variable `globalVar` is not properly marked as potentially reassignable, which can cause issues with live bindings and dead code elimination.

### Expected behavior

Global variables should be treated as live bindings since they can be reassigned at any time from outside the module scope. The bundler should not make assumptions about their immutability.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
