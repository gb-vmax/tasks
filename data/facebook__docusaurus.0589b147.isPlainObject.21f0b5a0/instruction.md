# Bug Report

### Describe the bug

I'm encountering an issue where objects that shouldn't be considered plain objects are being incorrectly identified as plain objects. Specifically, iterable objects (those with `Symbol.iterator`) are now being treated as plain objects when they shouldn't be.

### Reproduction

```js
// This should NOT be considered a plain object, but currently is
const iterableObj = {
  data: [1, 2, 3],
  [Symbol.iterator]: function* () {
    yield* this.data;
  }
};

// Expected: false (it has Symbol.iterator, so it's not a plain object)
// Actual: true (incorrectly identified as plain object)
console.log(isPlainObject(iterableObj));
```

Additionally, objects with `null` prototype are being handled inconsistently:

```js
const nullProtoObj = Object.create(null);
nullProtoObj.foo = 'bar';

// This might also be affected by the change
console.log(isPlainObject(nullProtoObj));
```

### Expected behavior

Objects with `Symbol.iterator` should NOT be considered plain objects, as they have special iteration behavior. The function should return `false` for any object that implements the iterator protocol.

Also, the prototype check should use strict equality (`===`) to properly distinguish between `null` and `undefined`.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
