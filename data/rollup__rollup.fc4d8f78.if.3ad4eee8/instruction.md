# Bug Report

### Describe the bug

I'm experiencing an issue with re-exports in my project. When using `export * from 'external-module'`, the imports are not resolving correctly. It seems like the module resolution is broken for namespace re-exports from external modules.

### Reproduction

```js
// lib.js
export * from 'external-package';

// main.js
import { something } from './lib.js';
```

When trying to import from a module that re-exports everything from an external package, the resolution fails or produces unexpected results. This is affecting my ability to create barrel exports that aggregate external dependencies.

### Expected behavior

Re-exporting from external modules using `export *` should work correctly and allow consumers to import the re-exported bindings without issues.

### Additional context

This seems to be related to how namespace exports are handled internally. The issue appears specifically when re-exporting from external modules (not local files).

---
Repository: /testbed
