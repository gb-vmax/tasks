# Bug Report

### Describe the bug

I'm encountering an issue where function parameters are being incorrectly marked as reassigned when they shouldn't be. This causes the bundler to be overly conservative and miss optimization opportunities.

### Reproduction

```js
function example(param) {
  // Call the function multiple times with the same literal value
  return param.value;
}

// These calls should be recognized as having the same known value
example({ value: 42 });
example({ value: 42 });
```

When a function is called multiple times with the same literal argument value, the parameter should maintain its known value. However, it appears that the parameter is being marked as reassigned even when the argument values are equivalent.

### Expected behavior

The parameter variable should only be marked as reassigned when it receives different values across function calls. When the same literal value is passed multiple times, the known value should be preserved to allow for better optimization.

### Additional context

This seems to affect tree-shaking and dead code elimination, as the bundler can't make assumptions about parameter values that should be trackable. The issue appears to be related to how argument entities are being tracked and compared.

---
Repository: /testbed
