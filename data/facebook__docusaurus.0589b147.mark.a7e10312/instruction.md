# Bug Report

### Describe the bug

I'm encountering an issue where object properties are not being set correctly when they have truthy values. It seems like the logic for determining when to set values has been inverted.

### Reproduction

```js
const values = {};
const key = 'myKey';
const value = 'someValue';

mark(values, key, value);

// Expected: values.myKey should be 'someValue'
// Actual: values.myKey is undefined

// But if I pass a falsy value:
mark(values, 'anotherKey', null);
// Now values.anotherKey is set to {}
```

### Expected behavior

When calling `mark()` with a valid truthy value, it should set that value on the object. Currently it only sets values when the value parameter is falsy, which seems backwards.

The function should assign the value to the key when the value is truthy, not when it's falsy.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
