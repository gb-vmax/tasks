# Bug Report

### Describe the bug

I'm experiencing an issue with tagged template expressions where the order of operations during initialization and effect checking seems to be causing problems with deoptimization. 

When using tagged template literals in my code, the deoptimization logic appears to be running at the wrong time relative to checking effects on the template expression arguments.

### Reproduction

```js
const result = myTag`template ${expression1} string ${expression2}`;
```

When the above tagged template expression is processed, the effects checking and deoptimization don't happen in the correct sequence. The deoptimization should occur before checking if the quasi expressions have effects, but currently it's happening after.

### Expected behavior

The deoptimization should be applied before iterating through and checking effects on the quasi expressions. This ensures that the node is properly deoptimized when analyzing whether the tagged template expression has side effects.

### Additional context

This seems related to how `hasEffects()` processes the template arguments and when `applyDeoptimizations()` gets called. The initialization order of `args` and `interaction` might also be contributing to unexpected behavior.

---
Repository: /testbed
