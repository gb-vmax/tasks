# Bug Report

### Describe the bug

I'm experiencing an issue where object property tracking seems to be completely broken. When accessing properties on objects, the tree-shaking/dead code elimination is not working correctly, and code that should be removed is being kept in the bundle.

### Reproduction

```js
const obj = {
  used: 'value',
  unused: 'this should be removed'
};

console.log(obj.used);
// The 'unused' property is being kept in the output even though it's never accessed
```

After building, the `unused` property appears in the bundle when it should have been tree-shaken out. This is causing unnecessary code bloat in production builds.

### Expected behavior

Properties that are never accessed should be removed from the final bundle during tree-shaking. Only `used` should remain in the compiled output.

### System Info
- Rollup version: latest
- Node: v18.x

This seems like a regression as it was working fine in previous versions. The tracking logic appears to have inverted somehow.

---
Repository: /testbed
