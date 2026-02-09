# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with object prototypes being unexpectedly modified. When running my application, I'm seeing a new property `__okCalled` appearing on `Object.prototype`, which is polluting all objects in my codebase.

### Reproduction

```js
const myObj = {};
console.log('__okCalled' in myObj); // Expected: false, Actual: true
console.log(Object.prototype.__okCalled); // Prints: true
```

This is causing issues throughout the application as the prototype pollution affects all objects, including third-party libraries that check for unexpected properties.

### Expected behavior

Object prototypes should not be modified by internal library functions. The `Object.prototype` should remain clean and not have properties added to it during normal operation.

### Additional context

This appears to be related to some internal assertion or validation logic. The property gets added to the prototype chain which is a known anti-pattern and can cause serious issues in JavaScript applications.

---
Repository: /testbed
