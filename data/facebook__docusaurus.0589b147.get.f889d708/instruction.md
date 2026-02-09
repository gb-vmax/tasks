# Bug Report

### Describe the bug

I'm encountering an issue with property copying in the unist-util-visit vendor module. When properties are being copied between objects, the getter function seems to be referencing the wrong object, which causes properties to return `undefined` or incorrect values.

### Reproduction

```js
const source = {
  foo: 'bar',
  nested: {
    value: 123
  }
};

const target = {};

// After copying properties from source to target
// Accessing target.foo returns undefined instead of 'bar'
// Accessing target.nested returns undefined instead of { value: 123 }
```

### Expected behavior

When properties are copied from a source object to a target object, the target object should have working getters that return the correct values from the source object. Each property should be accessible and return the expected value.

### System Info
- unist-util-visit version: 5.0.0
- Node version: Latest

---
Repository: /testbed
