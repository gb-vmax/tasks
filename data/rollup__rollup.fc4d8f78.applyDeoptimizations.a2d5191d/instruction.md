# Bug Report

### Describe the bug

I'm experiencing an issue with update expressions (`++` and `--` operators) where the order of deoptimization operations appears to cause incorrect behavior. When using increment/decrement operators on identifiers, the variable is being marked as reassigned before the argument's path is deoptimized, which can lead to unexpected results in certain edge cases.

### Reproduction

```js
let counter = 0;

function incrementCounter() {
  counter++;
  return counter;
}

// The deoptimization happens in the wrong order
// causing the variable state to be inconsistent
```

This seems to affect how the AST handles update expressions, particularly when the argument needs to be deoptimized before marking the variable as reassigned.

### Expected behavior

The deoptimization should happen in a consistent order:
1. Mark the variable as deoptimized
2. Deoptimize the argument path
3. Mark the variable as reassigned
4. Request treeshaking pass

Currently it seems like step 2 is happening after step 3, which can cause issues with how the variable state is tracked.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
