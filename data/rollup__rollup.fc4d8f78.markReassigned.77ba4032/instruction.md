# Bug Report

### Describe the bug

I'm experiencing an issue where parameter variables that get reassigned are not properly deoptimizing dependent expressions. It seems like when a parameter is marked as reassigned, the expressions that depend on knowing the parameter's value aren't being invalidated correctly.

### Reproduction

```js
function example(param) {
  // Some code that depends on param's known value
  const derived = param.someProperty;
  
  // Reassign the parameter
  param = someOtherValue;
  
  // Expressions that depended on the original param value
  // should be deoptimized but aren't being handled properly
  return derived;
}
```

### Expected behavior

When a parameter variable is reassigned, all expressions that were depending on the parameter's known value should have their caches deoptimized before the reassignment tracking is updated. This ensures that any optimizations made based on the original parameter value are properly invalidated.

### Additional context

This appears to affect how the bundler handles optimization of code that reassigns function parameters. The expressions depending on the parameter's value may retain incorrect cached optimization information.

---
Repository: /testbed
