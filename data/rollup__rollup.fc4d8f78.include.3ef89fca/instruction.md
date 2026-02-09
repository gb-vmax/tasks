# Bug Report

### Describe the bug

I'm experiencing an issue with return statements in functions where side effects in the return expression are being executed multiple times. It seems like the return argument is being included/processed more than once during tree-shaking or code generation.

### Reproduction

```js
function test() {
  let counter = 0;
  
  function sideEffect() {
    counter++;
    return counter;
  }
  
  return sideEffect();
}

// The sideEffect function appears to be called multiple times
// Expected: counter increments once
// Actual: counter increments more than once
```

### Expected behavior

The return statement's argument should only be evaluated/included once. Side effects in return expressions should execute exactly once, not multiple times.

### Additional context

This seems to happen specifically with return statements that have expressions with side effects. Simple return values work fine, but any function calls or operations in the return expression get processed multiple times.

---
Repository: /testbed
