# Bug Report

### Describe the bug

Optional chaining with function calls is not being tree-shaken correctly. When using optional chaining on a function call (e.g., `foo?.()`) where the callee is a non-null/undefined value, the code is incorrectly being removed during tree-shaking even though it should be included in the bundle.

### Reproduction

```js
const obj = {
  method: () => {
    console.log('side effect');
  }
};

// This call should be included in the bundle
obj.method?.();
```

After bundling, the function call is removed from the output even though `obj.method` is clearly not null/undefined and the function has side effects.

### Expected behavior

The optional chained function call should be preserved in the bundle when the callee is a known non-null/undefined value, especially when it has side effects. The tree-shaker should only skip the call if the callee is actually null or undefined.

### Additional context

This seems to affect optional call expressions specifically. Regular optional property access (like `obj?.prop`) works as expected, but optional function calls (`obj?.method()`) are being incorrectly eliminated.

---
Repository: /testbed
