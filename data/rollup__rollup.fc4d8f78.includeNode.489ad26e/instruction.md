# Bug Report

### Describe the bug

I'm encountering a crash when bundling code that contains object expressions without a `__proto__` property. The bundler throws an error trying to access properties on `undefined`.

### Reproduction

```js
// This works fine
const obj1 = {
  __proto__: null,
  foo: 'bar'
}

// This causes a crash during bundling
const obj2 = {
  foo: 'bar',
  baz: 'qux'
}
```

The issue seems to happen specifically when the object doesn't have a `__proto__` property defined. Regular object literals without an explicit proto property are failing to bundle.

### Expected behavior

Both object expressions should bundle successfully. Objects without an explicit `__proto__` property are extremely common and should be handled gracefully.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
