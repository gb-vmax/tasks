# Bug Report

### Describe the bug

The `__copyProps` helper function in the vendored mdast-util-to-string module is not copying properties correctly. When attempting to copy properties from source objects, the function seems to skip over valid properties that should be copied.

### Reproduction

```js
const source = {
  someMethod: function() { return 'test'; },
  someProperty: 'value'
};

const target = {};

// Properties are not being copied as expected
__copyProps(target, source);

console.log(target.someMethod); // Expected: function, Actual: undefined
console.log(target.someProperty); // Expected: 'value', Actual: undefined
```

### Expected behavior

The `__copyProps` function should correctly identify and copy properties from objects and functions to the target object. Both regular objects and function objects should have their properties enumerated and copied.

### Additional context

This appears to be related to the type checking logic in the `__copyProps` helper. The condition for determining whether to iterate over properties may not be evaluating correctly for certain object types.

---
Repository: /testbed
