# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying in the remark vendor bundle. When properties are being copied from one object to another, the getter functions are incorrectly referencing the target object instead of the source object. This causes a stack overflow error when trying to access the copied properties.

### Reproduction

```js
const source = {
  value: 'original'
};

const target = {};

// Copy properties using the __copyProps mechanism
__copyProps(target, source);

// Trying to access the copied property causes infinite recursion
console.log(target.value); // RangeError: Maximum call stack size exceeded
```

The getter defined for the copied property is calling `to[key]` instead of `from[key]`, which creates an infinite loop where the getter keeps calling itself.

### Expected behavior

The copied property should return the value from the source object. Accessing `target.value` should return `'original'` without any errors.

### System Info
- remark version: 15.0.1
- Node.js version: Latest

This seems to be affecting the property enumeration logic as well, where the enumerable check appears to be inverted.

---
Repository: /testbed
