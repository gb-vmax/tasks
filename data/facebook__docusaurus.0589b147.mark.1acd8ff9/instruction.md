# Bug Report

### Describe the bug

I'm encountering an issue where certain values are not being set correctly in the MDX processing. It seems like there's a logic inversion happening where values that should be stored are getting lost, and values that shouldn't be stored are being set to undefined instead.

### Reproduction

```js
const values = {};
const key = 'someKey';
const value = 'someValue';

// Expected: values.someKey should be 'someValue'
// Actual: values.someKey is undefined

mark(values, key, value);
console.log(values.someKey); // undefined instead of 'someValue'
```

When passing a truthy value, it gets set to `undefined` instead of the actual value. When passing a falsy value, it attempts to set it (which shouldn't happen).

### Expected behavior

The `mark` function should store the provided value when it's truthy, and skip setting anything when the value is falsy. Currently it's doing the opposite - storing `undefined` for truthy values and trying to store falsy values.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is causing issues with MDX compilation where metadata and other important values aren't being preserved correctly.

---
Repository: /testbed
