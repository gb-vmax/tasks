# Bug Report

### Describe the bug

Optional chaining on function calls is not working correctly. When using the `?.()` syntax with a potentially null/undefined callee, the code behaves as if the call always happens regardless of whether the callee exists or not.

### Reproduction

```js
const obj = {
  method: null
};

// This should short-circuit and not execute, but it doesn't
obj.method?.();

// Another example with nested properties
const data = {
  user: undefined
};

// Should safely handle undefined, but throws error instead
data.user?.getProfile?.();
```

### Expected behavior

When using optional chaining with function calls, if the callee is `null` or `undefined`, the expression should short-circuit and return `undefined` without attempting to execute the function. The current behavior seems to ignore the optional chaining and tries to execute anyway.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
