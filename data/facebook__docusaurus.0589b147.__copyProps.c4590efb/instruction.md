# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with module exports and property copying. Objects and functions that should be exported and accessible are no longer working correctly. It seems like the property enumeration logic has changed in an unexpected way.

### Reproduction

```js
// Create a module with various exports
const sourceModule = {
  myFunction: function() { return 'test'; },
  myObject: { value: 42 },
  myValue: 'hello'
};

// Try to copy properties to a new object
const targetModule = {};
// Properties are not being copied as expected
```

When trying to use exported functions or objects from modules, they're not available on the target object. This is breaking module imports and exports across the application.

### Expected behavior

All enumerable properties from source objects/modules should be properly copied to the target, regardless of whether they are objects, functions, or primitive values. The property descriptor's enumerable flag should be respected correctly.

### System Info
- Node version: 18.x
- Environment: Jest testing environment

---
Repository: /testbed
