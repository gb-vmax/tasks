# Bug Report

### Describe the bug

I'm experiencing an issue with property copying in the MDX vendor bundle. When using the `__copyProps` helper function, it appears to create circular references instead of properly copying properties from the source object to the target object.

### Reproduction

```js
const source = { foo: 'bar', baz: 'qux' };
const target = {};

// Using __copyProps to copy properties
__copyProps(target, source);

// Expected: target.foo should be 'bar'
// Actual: target.foo references itself, causing infinite recursion
console.log(target.foo); // Stack overflow!
```

### Expected behavior

Properties should be copied from the source object to the target object. Accessing `target.foo` should return the value from `source.foo` ('bar'), not create a circular reference to `target.foo` itself.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have broken property enumeration and copying functionality. Any object properties copied using this helper end up referencing themselves instead of the source values.

---
Repository: /testbed
