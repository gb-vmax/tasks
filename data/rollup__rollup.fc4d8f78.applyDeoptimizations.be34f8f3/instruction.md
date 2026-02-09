# Bug Report

### Describe the bug

I'm experiencing an issue with `for...in` loops where the iteration variable is not being properly tracked for side effects. When the iterable object (right-hand side) is mutated or has side effects, those changes aren't being detected, leading to incorrect tree-shaking behavior.

### Reproduction

```js
const obj = {
  get items() {
    // Side effect that should be tracked
    console.log('accessing items');
    return { a: 1, b: 2 };
  }
};

for (const key in obj.items) {
  // The getter on obj.items should be preserved
  console.log(key);
}
```

### Expected behavior

The code should properly track side effects on the iterable expression (the right-hand side of `for...in`). Any getters, function calls, or other side effects in the expression being iterated over should be preserved during tree-shaking.

Currently, it seems like only the left-hand side (the iteration variable) is being deoptimized, but the right-hand side expression isn't being tracked correctly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
