# Bug Report

### Describe the bug

I'm encountering an issue with the `isPlainObject` function where it's incorrectly identifying objects. The function seems to be returning `true` for objects that shouldn't be considered plain objects, and it's also not properly handling `null` values.

### Reproduction

```js
const obj = { foo: 'bar' };
const result = isPlainObject(obj);
// Expected: true
// Actual: false (when obj is null, it returns true incorrectly)

const iterableObj = {
  [Symbol.iterator]: function* () {
    yield 1;
  }
};
const result2 = isPlainObject(iterableObj);
// Expected: false (should not be plain object if it has Symbol.iterator)
// Actual: true
```

### Expected behavior

- `isPlainObject(null)` should return `false`
- Objects with `Symbol.iterator` should NOT be considered plain objects
- Regular plain objects like `{ foo: 'bar' }` should return `true`

The current behavior is inverted - it's treating null as a valid object and accepting iterable objects as plain objects, which breaks the expected semantics.

### System Info
- Node version: 18.x
- Package: estree-util-value-to-estree@3.0.1

---
Repository: /testbed
