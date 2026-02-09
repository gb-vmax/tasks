# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with object property copying in the mdast-util-to-string vendor module. It seems like properties from source objects are no longer being copied correctly to target objects.

### Reproduction

```js
const source = {
  prop1: 'value1',
  prop2: 'value2'
};

const target = {};

// Attempting to copy properties from source to target
// Properties are not being copied as expected
```

When trying to copy properties from one object to another, the target object remains empty or doesn't receive the expected properties. This is affecting the markdown AST string conversion functionality.

### Expected behavior

Properties should be properly copied from source objects to target objects, including their enumerable descriptors. The property copying mechanism should work for both regular objects and functions.

### System Info
- Module: mdast-util-to-string@4.0.0
- Node version: Latest

---
Repository: /testbed
