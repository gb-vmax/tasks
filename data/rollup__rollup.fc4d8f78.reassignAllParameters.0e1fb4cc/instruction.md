# Bug Report

### Describe the bug

I've noticed that when using function parameters in certain contexts, the first parameter is not being properly tracked for reassignments. This causes issues with parameter mutation detection and can lead to incorrect optimization behavior.

### Reproduction

```js
function example(first, second, third) {
  first = 'modified';
  second = 'also modified';
  third = 'changed too';
  return first + second + third;
}
```

In this case, all three parameters are reassigned, but it seems like only `second` and `third` are being tracked as reassigned while `first` is being skipped. This affects how the function is analyzed and optimized.

### Expected behavior

All parameters that are reassigned within a function body should be marked as reassigned, including the first parameter. The tracking should treat all parameters consistently regardless of their position.

### Additional context

This seems to affect functions with multiple parameters where reassignment tracking is important for optimization decisions. The issue appears to be specific to how parameters are being iterated over during the reassignment marking phase.

---
Repository: /testbed
