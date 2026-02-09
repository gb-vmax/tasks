# Bug Report

### Describe the bug

I'm experiencing an issue with array expressions where side effects are not being tracked correctly. It seems like operations on array elements are being treated as having no effects when they should, and conversely, some operations that should have effects are being reported incorrectly.

### Reproduction

```js
const arr = [obj1, obj2, obj3];

// Accessing array elements and calling methods on them
arr[0].someMethod();  // This should be tracked for side effects but isn't

// Also seeing inverted behavior where pure operations are flagged as having effects
const value = arr.length;  // This is being treated incorrectly
```

The problem appears to be related to how array expressions handle interaction paths. When accessing nested properties or calling methods on array elements, the side effect analysis seems to be backwards or skipped entirely.

### Expected behavior

Array element access and method calls should properly track whether they have side effects. Pure property reads shouldn't be flagged as having effects, while actual method calls or mutations should be properly detected.

### System Info
- Version: Latest from main branch
- Node version: 18.x

This is causing issues with tree-shaking and dead code elimination in my project. Any help would be appreciated!

---
Repository: /testbed
