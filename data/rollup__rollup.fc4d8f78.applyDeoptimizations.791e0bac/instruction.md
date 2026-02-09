# Bug Report

### Describe the bug

I'm experiencing an issue with the `delete` operator where it seems to be triggering unnecessary tree-shaking passes and deoptimizations. After a recent change, code that uses `delete` on object properties is behaving differently than expected.

### Reproduction

```js
const obj = { a: 1, b: 2, c: 3 };

function test() {
  delete obj.a;
  return obj;
}

// The delete operation seems to be causing unexpected side effects
// with tree-shaking and optimization
```

When using the `delete` operator on object properties, the behavior has changed. It appears that the deoptimization logic is now being applied incorrectly - the paths that should be deoptimized for `delete` operations are being deoptimized for other unary operators instead, while `delete` itself is skipping the deoptimization step.

### Expected behavior

The `delete` operator should properly deoptimize the argument path and request a tree-shaking pass, while other unary operators (like `void`, `typeof`, etc.) should not trigger these actions.

### Additional context

This seems to have started happening recently. The logic for when to deoptimize paths and request tree-shaking passes appears to be inverted for the `delete` operator compared to other unary operators.

---
Repository: /testbed
