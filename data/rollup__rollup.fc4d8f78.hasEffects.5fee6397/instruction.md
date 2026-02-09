# Bug Report

### Describe the bug

I'm encountering an issue where side effects in assignment expressions are being evaluated in the wrong order. When an assignment has both left-hand side effects and right-hand side effects, the right-hand side is being evaluated before the left-hand side, which doesn't match JavaScript's evaluation order.

### Reproduction

```js
let counter = 0;

function sideEffect() {
  counter++;
  return counter;
}

// The left side should be evaluated first, then the right side
obj[sideEffect()] = sideEffect();

// Expected: counter === 2
// Left side evaluated first (counter becomes 1)
// Right side evaluated second (counter becomes 2)
```

In the above example, JavaScript should evaluate the left-hand side of the assignment (the property access) before evaluating the right-hand side (the value being assigned). However, it seems like the evaluation order has been reversed.

### Expected behavior

Assignment expressions should evaluate their left-hand side before their right-hand side, following JavaScript semantics. Any side effects from evaluating the property/member access should occur before side effects from evaluating the assigned value.

### Additional context

This affects any assignment where both sides have observable side effects, including:
- Property assignments with computed keys
- Destructuring assignments
- Compound assignments

The evaluation order is important for correctness and matches the ECMAScript specification.

---
Repository: /testbed
