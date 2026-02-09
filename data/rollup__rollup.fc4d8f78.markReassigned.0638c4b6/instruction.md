# Bug Report

### Describe the bug

I'm experiencing an issue where parameter variables that are reassigned multiple times cause incorrect behavior. It seems like the deoptimization logic isn't being applied properly when a parameter is marked as reassigned more than once.

### Reproduction

```js
function example(param) {
  param = 'first reassignment';
  // ... some code that depends on param value
  param = 'second reassignment';
  // The expressions that depend on the parameter value 
  // don't get properly deoptimized on subsequent reassignments
  return param;
}
```

When a parameter variable is reassigned multiple times in the same function, only the first reassignment seems to trigger the proper deoptimization of dependent expressions. Subsequent reassignments don't update the cache correctly.

### Expected behavior

Each time a parameter is reassigned, all expressions that depend on knowing its value should be deoptimized and have their caches invalidated, regardless of whether it's the first or subsequent reassignment.

### Additional context

This appears to affect any function where parameters are reassigned multiple times, and there are expressions elsewhere in the code that depend on tracking the parameter's value. The optimization assumptions made about the parameter should be cleared every time it's reassigned, not just the first time.

---
Repository: /testbed
