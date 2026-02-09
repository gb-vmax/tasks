# Bug Report

### Describe the bug

I'm experiencing an issue with the SDK where methods on `PropertyBase` objects appear to be incomplete or truncated. When trying to use parent traversal methods like `findInParents()`, the behavior seems broken or the method doesn't complete its execution properly.

### Reproduction

```js
const property = new PropertyBase('test');
// Set up a parent hierarchy
property._parent = new PropertyBase('parent');

// Try to find a property in parents
const result = property.findInParents('someProperty');
// Expected to traverse parent chain and return matching parent
// Instead, the method seems to not complete properly
```

### Expected behavior

The `findInParents()` method should:
1. Traverse the parent hierarchy
2. Check each ancestor for the specified property
3. Return the first matching ancestor or undefined if not found
4. Support custom matching logic via the customizer function

Currently, it seems like the method implementation is cut off or incomplete, leading to unexpected behavior when traversing parent objects.

### System Info
- Package: insomnia-sdk
- Node version: 18.x

---
Repository: /testbed
