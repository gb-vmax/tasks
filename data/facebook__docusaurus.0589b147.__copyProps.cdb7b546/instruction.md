# Bug Report

### Describe the bug
After a recent update, I'm experiencing issues with object property copying in the remark-directive vendor code. It seems like properties aren't being copied correctly from source objects, which is breaking functionality that depends on this utility function.

### Reproduction
```js
// When trying to copy properties from an object to another
const source = {
  someMethod: function() { return 'test'; },
  someProperty: 'value'
};

const target = {};

// Properties should be copied but they're not showing up on the target
// The __copyProps utility seems to be failing silently
```

### Expected behavior
Properties from the source object should be properly copied to the target object, including both methods and regular properties. The enumerable descriptor should also be correctly set based on the source property's descriptor.

### System Info
- Version: Latest remark-directive vendor bundle (3.0.0)
- Node version: 18+

---
Repository: /testbed
