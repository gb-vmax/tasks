# Bug Report

### Describe the bug

The order of module importers returned by the plugin API seems to have changed unexpectedly. Previously, importers were returned in a simple sorted order, but now entry point modules appear to be prioritized and sorted separately from regular importers.

### Reproduction

```js
// In a plugin hook
this.load = function(id) {
  const moduleInfo = this.getModuleInfo(id);
  console.log(moduleInfo.importers);
  // Expected: ['a.js', 'b.js', 'entry.js'] (alphabetically sorted)
  // Actual: ['entry.js', 'a.js', 'b.js'] (entry points first, then others)
}
```

### Steps to reproduce:
1. Create a module that is imported by both an entry point and regular modules
2. Access the `importers` property via `getModuleInfo()` in a plugin hook
3. Observe that entry point importers are listed first, separate from other importers

### Expected behavior

The `importers` array should be sorted alphabetically regardless of whether an importer is an entry point or not. This was the previous behavior and changing it breaks plugins that rely on consistent ordering.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
