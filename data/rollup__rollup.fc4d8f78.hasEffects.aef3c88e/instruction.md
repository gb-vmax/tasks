# Bug Report

### Describe the bug

I'm experiencing an issue with dead code elimination in return statements. It seems like code after a return statement inside a function is being incorrectly removed even when the return statement itself should be eliminated due to tree-shaking.

### Reproduction

```js
function example() {
  return; // This return should be removed during tree-shaking
  sideEffect(); // This code should be kept because the return is eliminated
}
```

When the return statement is supposed to be tree-shaken away (ignored), any code following it is incorrectly being treated as unreachable and removed from the bundle. The side effects that should execute are being eliminated.

### Expected behavior

When a return statement is being ignored during tree-shaking analysis (e.g., in dead code paths), the control flow should not be marked as broken, allowing subsequent statements to be properly analyzed for side effects. Code with side effects after an ignored return should still be included in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
