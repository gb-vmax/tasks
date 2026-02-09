# Bug Report

### Describe the bug

Dynamic imports are not being detected properly in the module graph analysis. When a module is dynamically imported, it should be added to the dynamic entry modules set, but it seems like modules that should be included are being skipped.

### Reproduction

```js
// entry.js
import('./dynamic-module.js');

// dynamic-module.js
export default function() {
  console.log('Dynamic module loaded');
}
```

When building with the above setup, the dynamic module is not being properly tracked as a dynamic entry point even though it has dynamic importers.

### Expected behavior

Modules that are dynamically imported should be added to `dynamicEntryModules` and tracked in `allEntriesSet`. The current behavior seems to exclude valid dynamic entry modules from the chunk assignment process.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
