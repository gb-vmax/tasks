# Bug Report

### Describe the bug

I'm experiencing an issue where function arguments are not being properly tracked for deoptimization in certain scenarios. When working with call expressions that have arguments that need to be deoptimized, it seems like the deoptimization tracking is happening at the wrong time, causing some expressions to not be added to the tracking set before they're needed.

### Reproduction

```js
// Example scenario where this manifests:
function foo(obj) {
  return obj.method();
}

// When analyzing this code, arguments that should be tracked
// for deoptimization are not being registered properly
const result = foo(someObject);
```

The issue appears when:
1. A call expression has arguments that need deoptimization tracking
2. The return expression is not UNKNOWN_EXPRESSION
3. The arguments should be added to `expressionsToBeDeoptimized` before the recursive deoptimization call

### Expected behavior

All arguments that require deoptimization should be properly tracked and added to the deoptimization set regardless of when the recursive deoptimization happens. The tracking should ensure that expressions are registered before any recursive processing occurs.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
