# Bug Report

### Describe the bug

The `isPlainObject` function is not correctly identifying plain objects anymore. It seems to be rejecting valid plain objects and potentially accepting objects that shouldn't be considered plain objects.

### Reproduction

```js
const obj = { foo: 'bar' };
const result = isPlainObject(obj);
// Returns false, but should return true

const plainObj = Object.create(null);
plainObj.test = 'value';
const result2 = isPlainObject(plainObj);
// Returns false, but should return true for objects with null prototype
```

### Expected behavior

The function should return `true` for:
- Regular plain objects like `{ key: value }`
- Objects created with `Object.create(null)`
- Objects with `Object.prototype` as their prototype

It should return `false` for:
- Non-object values (null, undefined, primitives)
- Arrays
- Objects with custom prototypes beyond one level
- Objects with Symbol.iterator or Symbol.toStringTag

### Additional context

This appears to have broken after a recent change. The function is critical for distinguishing plain objects from other types, and the current behavior is causing issues with object serialization/conversion.

---
Repository: /testbed
