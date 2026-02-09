# Bug Report

### Describe the bug

I'm encountering an issue with property copying in the vendored remark-rehype module. When properties are being copied between objects, the getter functions are not accessing the correct source object, which leads to incorrect property values being returned.

### Reproduction

```js
const source = {
  foo: 'bar',
  baz: 'qux'
};

const target = {};

// After copying properties using __copyProps
// Accessing target.foo returns undefined or wrong value
// instead of 'bar'
```

### Expected behavior

When properties are copied from a source object to a target object, the getter should retrieve values from the source object, not from the target object itself. Each copied property should return the correct value from the original source.

### System Info
- Version: remark-rehype@11.0.0
- Node version: Latest

---
Repository: /testbed
