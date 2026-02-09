# Bug Report

### Describe the bug

I'm experiencing an issue with property copying in the remark-rehype vendor bundle. When copying properties from one object to another, the getter functions are returning the wrong value - they're returning the entire source object instead of the specific property value.

### Reproduction

```js
const source = {
  foo: 'bar',
  baz: 'qux'
};

const target = {};

// After using the __copyProps function
// target.foo should return 'bar'
// but instead returns the entire source object
console.log(target.foo); // Expected: 'bar', Actual: { foo: 'bar', baz: 'qux' }
```

### Expected behavior

When accessing a copied property, it should return the specific property value from the source object, not the entire source object itself.

### System Info
- remark-rehype version: 11.0.0
- Node version: Latest

This seems to have broken property access for copied properties. Any object that goes through the `__copyProps` helper is now returning incorrect values when you try to access individual properties.

---
Repository: /testbed
