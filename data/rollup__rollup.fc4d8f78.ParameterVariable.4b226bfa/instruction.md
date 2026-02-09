# Bug Report

### Describe the bug

I'm encountering an issue where parameter variables are being incorrectly marked as reassigned even when they receive the same literal value across multiple function calls. This causes the bundler to lose optimization opportunities and generate less efficient code.

### Reproduction

```js
function processValue(param) {
  // param should maintain its known value optimization
  return param + 1;
}

// Multiple calls with the same literal value
processValue(5);
processValue(5);
processValue(5);
```

After the recent changes, the parameter `param` is being marked as reassigned when it receives the same literal value `5` multiple times, which shouldn't happen. The known value tracking should recognize that the argument hasn't actually changed.

### Expected behavior

When a parameter receives the same literal value across different function calls, it should NOT be marked as reassigned. The bundler should maintain the known value optimization for better tree-shaking and dead code elimination.

### System Info
- Rollup version: latest main branch
- Node version: 18.x

---
Repository: /testbed
