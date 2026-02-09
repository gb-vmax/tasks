# Bug Report

### Describe the bug

I'm experiencing an issue with external module naming and importer ordering. When working with external modules, the suggested variable names seem incorrect and the order of importers/dynamicImporters appears to be reversed from what I'd expect.

### Reproduction

```js
// When importing an external module like 'lodash/debounce'
// The suggested variable name becomes 'lodash' instead of 'debounce'

// Also, when checking module info:
const moduleInfo = this.getModuleInfo(externalModuleId);
console.log(moduleInfo.importers);
// The importers array is in reverse order compared to previous versions
```

### Expected behavior

1. For a path like `lodash/debounce`, the suggested variable name should be `debounce` (the last segment), not `lodash` (the first segment)
2. The `importers` and `dynamicImporters` arrays should maintain their original order or be sorted alphabetically, not reversed

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have changed recently and is affecting our build output variable naming and module dependency tracking.

---
Repository: /testbed
