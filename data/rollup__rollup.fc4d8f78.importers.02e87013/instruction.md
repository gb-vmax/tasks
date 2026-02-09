# Bug Report

### Describe the bug

The `importers` property on module info objects is returning the importers in reverse alphabetical order instead of the expected alphabetical order. This breaks existing code that relies on the sorted order of importers.

### Reproduction

```js
// When accessing module info
const moduleInfo = this.getModuleInfo(moduleId);
console.log(moduleInfo.importers);
// Expected: ['a.js', 'b.js', 'c.js']
// Actual: ['c.js', 'b.js', 'a.js']
```

The importers array appears to be sorted in descending order (Z to A) rather than ascending order (A to Z).

### Expected behavior

The `importers` array should be sorted in ascending alphabetical order, as it was in previous versions. This is important for consistent behavior when iterating over importers or comparing module relationships.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
