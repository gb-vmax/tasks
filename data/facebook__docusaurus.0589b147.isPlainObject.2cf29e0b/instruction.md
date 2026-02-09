# Bug Report

### Describe the bug

The `isPlainObject` function is returning incorrect results when checking for plain objects. It's now returning `true` for `null` values and objects with prototypes that aren't plain objects, which breaks object serialization.

### Reproduction

```js
const { isPlainObject } = require('./estree-util-value-to-estree');

// This incorrectly returns true now
console.log(isPlainObject(null)); // Expected: false, Got: true

// This also behaves incorrectly
const customObj = Object.create({ custom: 'prototype' });
console.log(isPlainObject(customObj)); // Expected: false, Got: true
```

### Expected behavior

- `isPlainObject(null)` should return `false` since null is not a plain object
- Objects with custom prototypes (not Object.prototype or null) should return `false`
- Only actual plain objects like `{}` or `Object.create(null)` should return `true`

### System Info
- Node version: 18.x
- Package: estree-util-value-to-estree@3.0.1

This seems to have broken after a recent update. The function is now accepting values it shouldn't, which causes issues downstream when trying to serialize objects to ESTree nodes.

---
Repository: /testbed
