# Bug Report

### Describe the bug

I'm experiencing an infinite recursion issue that causes a stack overflow when using the mdast-util-to-string module. The application crashes with a "Maximum call stack size exceeded" error during property copying operations.

### Reproduction

```js
// When the module attempts to copy properties from one object to another,
// it enters an infinite loop and crashes

const mdastUtilToString = require('./mdast-util-to-string@4.0.0.js');

// Any operation that triggers the __copyProps function will fail
// For example, importing/using the module's exports
```

The error occurs internally when the property getter references itself instead of the source object, creating an infinite recursive loop.

### Expected behavior

The module should successfully copy properties from the source object to the target object without causing stack overflow errors. Property access should return values from the source object, not recursively reference the target object.

### System Info
- Node version: Latest
- Module: mdast-util-to-string@4.0.0

This is blocking our ability to use any markdown AST string conversion functionality. Any help would be appreciated!

---
Repository: /testbed
