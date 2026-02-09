# Bug Report

### Describe the bug

I'm experiencing an issue with property access in the MDX vendor bundle. When trying to access properties from copied objects, I'm getting unexpected `undefined` values instead of the actual property values.

### Reproduction

```js
const source = {
  foo: 'bar',
  nested: {
    value: 123
  }
};

const target = {};
// Using the __copyProps utility from the vendor bundle
__copyProps(target, source);

console.log(target.foo); // Expected: 'bar', Got: undefined
console.log(target.nested); // Expected: { value: 123 }, Got: undefined
```

### Expected behavior

Properties should be correctly copied and accessible from the target object. The getter should return the actual property value from the source object.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken after a recent change to the vendor bundle. The property copying mechanism is not working as expected.

---
Repository: /testbed
