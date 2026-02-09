# Bug Report

### Describe the bug

Dynamic imports are not being properly detected and added as entry modules when analyzing the module graph. It appears that modules that should be marked as dynamic entries are being skipped during the chunk assignment phase.

### Reproduction

When building a project with dynamic imports:

```js
// entry.js
import('./dynamic-module.js');

// dynamic-module.js
export default function() {
  console.log('Dynamic module loaded');
}
```

The dynamic module is not being included in the output chunks as expected. The module graph analysis seems to be incorrectly filtering out valid dynamic entry points.

### Expected behavior

Dynamic imports should be properly identified and included as dynamic entry modules in the chunk assignment process. Modules that are dynamically imported and have included dynamic importers should be added to the set of dynamic entry modules.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
