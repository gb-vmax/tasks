# Bug Report

### Describe the bug

I'm encountering an issue with the `mark` function in the MDX vendor bundle. When a falsy value is passed, the function is now setting the key to itself instead of doing nothing. This causes unexpected behavior where properties are being set when they shouldn't be.

### Reproduction

```js
const values = {};
mark(values, 'myKey', null);

// Expected: values should remain empty {}
// Actual: values = { myKey: 'myKey' }
```

The function appears to have inverted logic - it's now executing the assignment when the value is falsy instead of when it's truthy. This means:

1. Passing `null`, `undefined`, `false`, `0`, or empty string triggers the assignment
2. The key gets assigned to itself rather than the intended value
3. Passing a truthy value does nothing (opposite of expected)

### Expected behavior

The `mark` function should only set `values[key] = value` when `value` is truthy. Falsy values should be ignored and not modify the `values` object.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: 18.x

---
Repository: /testbed
