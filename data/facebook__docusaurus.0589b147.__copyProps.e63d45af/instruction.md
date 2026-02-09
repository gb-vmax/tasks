# Bug Report

### Describe the bug

I'm experiencing an issue with object property copying in the estree-util-value-to-estree vendor module. It seems like properties from regular objects are not being copied correctly anymore.

### Reproduction

```js
const source = {
  foo: 'bar',
  nested: {
    value: 42
  }
};

const target = {};

// Try to copy properties from source to target
// Properties are not being copied as expected
```

When trying to copy properties from a plain object to another object, the properties don't get transferred. This affects serialization of regular JavaScript objects.

### Expected behavior

Properties from objects (not just functions) should be copied to the target object. Both objects and functions should be handled correctly during the property copying process.

### Additional context

This seems to have broken after a recent update to the vendor module. The issue appears to be related to how the type checking logic determines whether to proceed with property enumeration.

---
Repository: /testbed
