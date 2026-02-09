# Bug Report

### Describe the bug

I'm encountering an issue with switch statement handling where the control flow analysis seems to be incorrect. When a switch statement has a default case but no matching regular cases, the broken flow state is not being properly tracked.

### Reproduction

```js
switch (someValue) {
  case 'a':
    return;
  case 'b':
    return;
  default:
    return;
}

// Code here should be recognized as unreachable
console.log('this should never execute');
```

The issue appears to be with how the default case is being handled in the control flow analysis. When all cases (including default) have `return` statements, the code following the switch should be detected as unreachable, but it's not being flagged correctly.

### Expected behavior

The bundler should correctly identify that code after a switch statement with a default case is unreachable when all branches break/return. This affects dead code elimination and tree-shaking optimizations.

### Additional context

This seems to affect switch statements where:
- A default case is present
- All cases have control flow statements (return, throw, etc.)
- No cases actually match at analysis time

The broken flow tracking appears to be inverted in some scenarios involving the default case.

---
Repository: /testbed
