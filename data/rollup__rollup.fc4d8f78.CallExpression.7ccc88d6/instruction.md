# Bug Report

### Describe the bug

Optional chaining on method calls is not working correctly. When using `?.()` syntax, the call is being executed even when the callee is `null` or `undefined`, which should instead short-circuit and skip the call entirely.

### Reproduction

```js
const obj = null;

// This should NOT execute the call and return undefined
// but instead the call is being executed
const result = obj?.someMethod();

// Similarly with nested optional chaining:
const data = {
  user: null
};

// This should short-circuit and return undefined
// but the method call is still attempted
data.user?.getName();
```

### Expected behavior

When using optional chaining with function calls (`?.()`), if the callee evaluates to `null` or `undefined`, the entire expression should short-circuit and return `undefined` without attempting to execute the call. The call should only be executed when the callee is NOT `null` or `undefined`.

This is standard JavaScript optional chaining behavior and seems to have broken recently.

---
Repository: /testbed
