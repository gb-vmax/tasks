# Bug Report

### Describe the bug

After a recent update, the `importedIdResolutions` property is returning objects with an additional `hasCustomAttributes` field that wasn't there before. This is breaking our build pipeline which expects the resolved IDs to match the original structure.

### Reproduction

```js
// When accessing module info
const moduleInfo = this.getModuleInfo(moduleId);
const resolutions = moduleInfo.importedIdResolutions;

// Each resolution now has an unexpected hasCustomAttributes property
console.log(resolutions[0]);
// Output: { id: '...', external: false, ..., hasCustomAttributes: true }
// Expected: { id: '...', external: false, ... }
```

### Expected behavior

The `importedIdResolutions` array should return the resolved ID objects as they are stored in `module.resolvedIds`, without adding extra properties. Our tooling relies on this structure and the additional field is causing type mismatches and validation errors.

### Additional context

This seems to have changed recently. Previously, the resolved IDs were returned directly without modification. Now they're being transformed with an extra property that we didn't request and don't need.

---
Repository: /testbed
