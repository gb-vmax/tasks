# Bug Report

### Describe the bug

I'm experiencing an issue where property access on certain object members is not being properly tree-shaken. Code that should be removed as dead code during the build process is being included in the final bundle.

### Reproduction

```js
// example.js
const obj = {
  usedProperty: 'used',
  unusedProperty: 'unused'
};

// Only accessing usedProperty
console.log(obj.usedProperty);

// The unusedProperty should be tree-shaken but isn't
```

When bundling this code, the `unusedProperty` is still present in the output even though it's never accessed. This is causing larger bundle sizes than expected.

### Expected behavior

Unused properties should be removed during tree-shaking. The final bundle should only contain code that is actually used.

### Additional context

This seems to affect member expressions where the property is not directly referenced. The tree-shaking optimization appears to not be triggering correctly for these cases.

---
Repository: /testbed
