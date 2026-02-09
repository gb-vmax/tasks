# Bug Report

### Describe the bug

I'm experiencing an issue where member expressions on undefined objects are not being included correctly in the bundle. When accessing properties on values that are undefined, the code path seems to be inverted - it's including the path when it should be skipping it, and vice versa.

### Reproduction

```js
// Example code that triggers the issue
const obj = undefined;
const result = obj?.someProperty;

// Or accessing a property that doesn't exist
const value = someObject.undefinedProperty.nestedAccess;
```

When bundling code that contains member expressions on undefined values, the resulting bundle either:
- Includes unnecessary code paths that should be tree-shaken
- Excludes necessary code paths that should be included

This seems to affect optional chaining and property access on potentially undefined objects.

### Expected behavior

Member expressions should correctly determine whether to include code paths based on whether the object is defined or undefined. Code that accesses properties on undefined values should be handled appropriately during the tree-shaking process.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
