# Bug Report

### Describe the bug

When querying module information for external modules, the `importers` array is returning incomplete data. It appears that the first and last importers are being excluded from the results.

### Reproduction

```js
// Given an external module with multiple importers
const moduleInfo = this.getModuleInfo('external-module');

// Expected: all importers that reference this module
// Actual: missing the first and last importer from the list
console.log(moduleInfo.importers);
// Output might be ['b.js', 'c.js'] when it should be ['a.js', 'b.js', 'c.js', 'd.js']
```

### Expected behavior

The `importers` property should return the complete list of all modules that import the external module, sorted alphabetically. Currently it seems like the first and last entries are being cut off.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
