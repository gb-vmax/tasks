# Bug Report

### Describe the bug

I'm encountering an issue with `importedIdResolutions` where it returns an array structure that doesn't match what I expect. The output seems to be double-wrapped in an array, which breaks downstream code that relies on this property.

### Reproduction

```js
// When accessing importedIdResolutions on a module
const resolutions = moduleInfo.importedIdResolutions;

// Expected: Array of resolution objects
// Actual: Array containing an array of resolution objects

// This causes issues when iterating:
resolutions.forEach(resolution => {
  // resolution is actually an array, not a resolution object
  console.log(resolution.id); // undefined
});
```

### Expected behavior

`importedIdResolutions` should return a flat array of resolved ID objects, not a nested array structure. The property should be directly iterable without needing to unwrap an extra array layer.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
