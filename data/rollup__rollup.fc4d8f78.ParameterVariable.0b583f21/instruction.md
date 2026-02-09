# Bug Report

### Describe the bug

I'm encountering an issue where parameter variables are being incorrectly marked as reassigned when they shouldn't be. This seems to affect the optimization logic in rollup, causing unnecessary deoptimizations.

### Reproduction

When a function parameter receives the same literal value across multiple calls, the parameter variable gets marked as reassigned even though the value hasn't actually changed.

```js
function test(param) {
  // param should maintain its known value optimization
  return param.property;
}

// Both calls pass the same literal value
test({ property: 'value' });
test({ property: 'value' });
```

After the second call, the parameter is marked as reassigned, which triggers deoptimization pathways that shouldn't be activated.

### Expected behavior

The parameter variable should only be marked as reassigned when it receives a *different* value, not when it receives the same literal value multiple times. The known value optimization should be preserved when the argument values are consistent.

### Additional context

This appears to be affecting the deoptimization logic - arguments that should be recognized as having consistent values are instead triggering full deoptimization of all interactions. The behavior seems inverted from what it should be.

---
Repository: /testbed
