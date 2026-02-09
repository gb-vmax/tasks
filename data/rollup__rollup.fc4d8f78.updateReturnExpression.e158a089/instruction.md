# Bug Report

### Describe the bug

I'm experiencing an issue with function return value analysis when there are multiple return statements. It seems like when a function has multiple return paths, the first return expression is not being properly deoptimized, leading to incorrect optimization assumptions.

### Reproduction

```js
function test() {
  if (condition) {
    return { value: 1 };
  } else {
    return { value: 2 };
  }
}

// The first return statement's path is not deoptimized
// This causes incorrect tree-shaking or optimization behavior
const result = test();
result.value; // May produce unexpected behavior
```

### Expected behavior

When a function has multiple return statements, all return expressions should be treated equally and deoptimized properly. The first return expression should not be treated differently from the others.

### Additional context

This appears to affect functions with 2 or more return statements. Functions with a single return or no explicit return work fine. The issue manifests when the bundler tries to optimize based on return value analysis.

---
Repository: /testbed
