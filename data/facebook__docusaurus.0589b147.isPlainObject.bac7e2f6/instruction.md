# Bug Report

### Describe the bug

The `isPlainObject` function is incorrectly identifying non-plain objects as plain objects. When passing `null` or objects with prototype chains, the function returns unexpected results.

### Reproduction

```js
// This should return false but returns true
isPlainObject(null)

// Objects with extended prototype chains are also misidentified
class MyClass {}
const instance = new MyClass()
// This should return false but may return true
isPlainObject(instance)
```

### Expected behavior

- `isPlainObject(null)` should return `false` since null is not a plain object
- Objects with custom prototype chains (like class instances) should return `false`
- Only actual plain objects like `{}` or `Object.create(null)` should return `true`

### System Info
- remark version: 15.0.1

---
Repository: /testbed
