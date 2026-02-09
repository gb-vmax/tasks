# Bug Report

### Describe the bug

I'm experiencing an issue where external module information is returning importers in an unexpected order. The `importers` array appears to be unsorted, which is causing inconsistent behavior across different runs and making it difficult to compare module metadata.

### Reproduction

```js
// When accessing external module info
const moduleInfo = this.getModuleInfo(externalModuleId);
console.log(moduleInfo.importers);
// Expected: sorted array of importer IDs
// Actual: unsorted array (insertion order)
```

The `importers` getter should return a sorted array for consistency, but it seems to be returning the raw array without sorting.

### Expected behavior

The `importers` property should return a consistently sorted array, similar to how `dynamicImporters` behaves. This is important for:
- Reproducible builds
- Consistent snapshots/tests
- Predictable output when comparing module graphs

### Additional context

This seems to affect external modules specifically. The behavior is inconsistent with the `dynamicImporters` property which does return sorted results.

---
Repository: /testbed
