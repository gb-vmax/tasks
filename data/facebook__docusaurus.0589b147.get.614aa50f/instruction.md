# Bug Report

### Describe the bug

I'm experiencing an issue with property copying/enumeration in the rehype-stringify vendor code. When copying properties from one object to another, the copied properties are returning `undefined` instead of their actual values.

### Reproduction

```js
const source = {
  foo: 'bar',
  baz: 123,
  nested: { value: 'test' }
}

const target = {}

// After copying properties using __copyProps
// Accessing target.foo returns undefined instead of 'bar'
// Accessing target.baz returns undefined instead of 123
```

### Expected behavior

When properties are copied from a source object to a target object, accessing those properties on the target should return the same values as the source object. The getter functions should correctly reference the source property values.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

This seems to be affecting property access after the copy operation. The properties appear to exist on the target object but their values are not being retrieved correctly.

---
Repository: /testbed
