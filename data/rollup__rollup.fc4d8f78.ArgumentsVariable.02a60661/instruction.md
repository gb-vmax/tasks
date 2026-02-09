# Bug Report

### Describe the bug

I'm encountering an issue with the `arguments` object deoptimization in function scopes. When a function references the `arguments` variable and certain code paths are included, the deoptimization seems to happen in the wrong order, causing arguments to not be properly tracked.

### Reproduction

```js
function test() {
  // Reference arguments to trigger deoptimization tracking
  console.log(arguments);
  
  // Some code that triggers includePath
  if (someCondition) {
    return arguments[0];
  }
}
```

When the code path is included during tree-shaking analysis, the arguments that should be deoptimized are being cleared before they're actually processed. This causes the deoptimization to not propagate correctly to the actual argument expressions.

### Expected behavior

All arguments should be properly deoptimized with `UNKNOWN_PATH` before the tracking array is cleared. The deoptimization should happen in the correct sequence to ensure all argument references are handled.

### Additional context

This seems to affect scenarios where:
1. A function uses the `arguments` object
2. The function body has conditional paths that get included during analysis
3. The arguments need to be deoptimized as part of the inclusion process

The order of operations during the inclusion phase appears to be critical here.

---
Repository: /testbed
