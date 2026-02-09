# Bug Report

### Describe the bug

I'm encountering an issue with object property copying in the vendored `unist-util-remove-position` module. It seems like properties are not being copied correctly from source objects, which is causing unexpected behavior in my code.

### Reproduction

```js
const sourceObj = {
  prop1: 'value1',
  prop2: 'value2',
  method: function() { return 'test'; }
};

const targetObj = {};

// After the copy operation, targetObj should have all properties from sourceObj
// but some properties are missing or not enumerable as expected
```

When I try to copy properties from objects that have methods or are function-like, the properties don't get transferred properly. This is affecting the AST manipulation functionality.

### Expected behavior

All enumerable properties from the source object should be copied to the target object, including both data properties and methods. The enumerable flag should be preserved correctly.

### System Info
- Node version: 18.x
- Package: unist-util-remove-position@5.0.0 (vendored)

---
Repository: /testbed
