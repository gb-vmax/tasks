# Bug Report

### Describe the bug

I'm experiencing an issue with `for...in` loops where the right-hand side expression is being evaluated in the wrong order. It seems like the right-hand side is now being evaluated after the loop body instead of before it, which causes problems when the right-hand side has side effects.

### Reproduction

```js
let sideEffectCount = 0;

function getRightSide() {
  sideEffectCount++;
  return { a: 1, b: 2 };
}

for (const key in getRightSide()) {
  // The side effect from getRightSide() should happen before the loop body executes
  console.log(sideEffectCount); // Expected: 1, but behavior suggests otherwise
}
```

The right-hand side expression should be evaluated before entering the loop body, but it appears the evaluation order has changed. This is particularly problematic when the right-hand side expression has side effects that should occur before any loop iterations.

### Expected behavior

The right-hand side of a `for...in` statement should be evaluated before the loop body executes, not after. Side effects from the right-hand side expression should occur in the correct order relative to the loop body.

### Additional context

This seems to have started happening recently. The evaluation order is critical for correctness when dealing with expressions that have side effects.

---
Repository: /testbed
