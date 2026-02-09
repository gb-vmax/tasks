# Bug Report

### Describe the bug

Optional chaining with method calls is not being handled correctly. When using the `?.()` syntax on a method call, the code is being executed even when the callee evaluates to `null` or `undefined`, which should short-circuit the entire expression.

### Reproduction

```js
const obj = null;

// This should not throw an error but does
const result = obj?.method();

// Similar issue with optional method calls on objects
const data = {
  user: null
};

// This throws instead of returning undefined
const name = data.user?.getName();
```

### Expected behavior

When using optional chaining with method calls (`?.()`), if the value before `?.` is `null` or `undefined`, the entire expression should evaluate to `undefined` without attempting to call the method. The call should be skipped entirely.

Currently, it appears the optional chaining is not properly short-circuiting method invocations, leading to runtime errors that shouldn't occur.

### Additional context

This seems to affect optional call expressions specifically. Regular optional property access (e.g., `obj?.prop`) works as expected, but combining it with function calls doesn't behave correctly.

---
Repository: /testbed
