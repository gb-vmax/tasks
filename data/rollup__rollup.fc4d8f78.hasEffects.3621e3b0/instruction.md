# Bug Report

### Describe the bug

Empty statements are being included in the output bundle even when they have no side effects and tree-shaking should remove them. This causes unnecessary bloat in the final bundle.

### Reproduction

```js
// input.js
function test() {
  ; // empty statement
  return 42;
}

; // another empty statement

export { test };
```

When bundling this code, the empty statements are being preserved in the output even though they serve no purpose and should be removed during tree-shaking.

### Expected behavior

Empty statements should be removed from the bundle since they have no effects and don't contribute to the program's functionality. The tree-shaking process should eliminate these as dead code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
