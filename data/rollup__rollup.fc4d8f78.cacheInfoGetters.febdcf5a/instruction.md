# Bug Report

### Describe the bug

I'm experiencing an issue with external module info caching. When accessing the `importers` property on external modules, it doesn't seem to be properly cached and returns incorrect or missing data.

### Reproduction

```js
// Create an external module
const externalMod = new ExternalModule({ ... });

// Try to access importers info
const importers = externalMod.info.importers;

// The importers property is not being cached correctly
// Expected the property to be cached but it's not accessible as expected
```

### Expected behavior

The `info` object's `importers` property should be properly cached and accessible. The caching mechanism should apply to the correct object level so that both `importers` and `dynamicImporters` are available when needed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
