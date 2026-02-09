# Bug Report

### Describe the bug

I'm encountering an issue with return statements in functions where the control flow tracking seems incorrect. When a return statement has side effects in its argument, the flow analysis doesn't properly mark the control flow as broken.

### Reproduction

```js
function test() {
  return sideEffect();
  unreachableCode(); // This should be detected as unreachable
}
```

The bundler isn't correctly identifying that code after a return statement with side-effectful arguments is unreachable. This appears to be affecting dead code elimination.

### Expected behavior

When a return statement is encountered (regardless of whether its argument has side effects), the control flow should be marked as broken immediately. Any code following the return should be properly identified as unreachable and potentially tree-shaken.

### Additional context

This seems related to how `hasEffects` handles the control flow state. The flow breaking should happen consistently for all return statements that have effects, not just in certain conditions.

---
Repository: /testbed
