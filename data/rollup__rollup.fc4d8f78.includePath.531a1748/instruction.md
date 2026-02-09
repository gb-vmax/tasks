# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where object properties are being incorrectly included in the bundle. It seems like when a property path is being traced through an object, the inclusion logic isn't working as expected and properties that should be tree-shaken are ending up in the final output.

### Reproduction

```js
// input.js
const obj = {
  used: {
    nested: 'value'
  },
  unused: {
    data: 'should be removed'
  }
};

export const result = obj.used.nested;
```

When bundling this code, I would expect only the `used` property and its nested structure to be included, but it appears that once a property is marked as included, subsequent path tracing doesn't work correctly.

### Expected behavior

Only the properties that are actually accessed should be included in the bundle. Unused properties should be tree-shaken out completely.

### Additional context

This appears to be related to how property inclusion is tracked when traversing nested object paths. The issue manifests when the same property is accessed multiple times through different code paths.

---
Repository: /testbed
