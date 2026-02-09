# Bug Report

### Describe the bug

I'm experiencing an issue where function parameters with constant values are being incorrectly marked as reassigned, which is preventing proper tree-shaking and optimization. This seems to be affecting dead code elimination when the same literal value is passed to a function parameter multiple times.

### Reproduction

```js
function processValue(value) {
  if (value === 'constant') {
    // This code should be kept
    return doSomething();
  } else {
    // This code should be eliminated
    return doSomethingElse();
  }
}

// All calls use the same constant value
processValue('constant');
processValue('constant');
processValue('constant');
```

### Expected behavior

When a parameter receives the same literal value across multiple calls, the parameter should maintain its known value and allow proper dead code elimination. The unreachable branches should be tree-shaken out.

### Actual behavior

The parameter is being marked as reassigned even though all calls pass the same constant value. This prevents optimization and results in unnecessary code being included in the bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
