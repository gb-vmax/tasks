# Bug Report

### Describe the bug

I'm experiencing an issue where parameter variables are being incorrectly marked as reassigned when they shouldn't be. This seems to be affecting tree-shaking and optimization behavior in my bundle.

### Reproduction

```js
function processValue(param) {
  // When the same literal value is passed multiple times,
  // the parameter is unexpectedly treated as reassigned
  return param.toString();
}

// These calls should recognize that param has consistent literal values
processValue(42);
processValue(42);
processValue(42);
```

The issue occurs when:
1. A function is called multiple times with the same literal value
2. The parameter should maintain its known value optimization
3. Instead, it's being marked as reassigned even though the value is consistent

### Expected behavior

When a parameter receives the same literal value across multiple calls, it should maintain its known value and not be marked as reassigned. This would allow for better optimization and tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
