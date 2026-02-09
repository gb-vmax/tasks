# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying where properties seem to reference themselves instead of the source object. This creates a circular reference that causes the copied object to behave incorrectly.

### Reproduction

```js
const source = {
  foo: 'bar',
  nested: {
    value: 42
  }
};

const target = {};

// After copying properties from source to target
// Accessing target.foo should return 'bar' from source
// But instead it returns undefined or causes infinite recursion
```

### Expected behavior

When copying properties from one object to another, the getter should retrieve values from the source object, not from the target object itself. The target object should act as a proper proxy/wrapper for the source object's properties.

### Additional context

This appears to affect property enumeration as well - the enumerable flag logic seems inverted, causing non-enumerable properties to become enumerable and vice versa.

---
Repository: /testbed
