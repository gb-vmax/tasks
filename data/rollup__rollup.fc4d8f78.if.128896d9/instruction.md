# Bug Report

### Describe the bug

I'm experiencing an issue with re-exports from external modules. When using `export * from 'external-package'`, the module resolution seems to be broken and I'm getting errors about variables not being found.

### Reproduction

```js
// moduleA.js
export * from 'some-external-package';

// main.js
import { someExport } from './moduleA';
```

When trying to import from a module that re-exports from an external package, the build fails or the wrong module is resolved. It seems like the module ID is not being extracted correctly when processing the re-export statement.

### Expected behavior

Re-exports from external modules should work correctly and resolve to the proper external package. The external module's exports should be accessible through the re-exporting module.

### Additional context

This appears to affect specifically the case where we're re-exporting all exports from an external module using the `export *` syntax. Direct re-exports of named exports seem to work fine, but the wildcard re-export is problematic.

---
Repository: /testbed
