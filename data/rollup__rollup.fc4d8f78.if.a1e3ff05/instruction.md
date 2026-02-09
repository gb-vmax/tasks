# Bug Report

### Describe the bug

I'm experiencing an issue with re-exports from external modules. When using `export * from 'external-package'`, the exported namespace is not being resolved correctly, leading to errors when trying to access the re-exported values.

### Reproduction

```js
// module-a.js
export * from 'some-external-package';

// main.js
import { someExport } from './module-a.js';
console.log(someExport); // Error or undefined
```

The re-export statement should properly forward all exports from the external module, but it seems like the namespace resolution is broken. This affects both named exports and namespace exports from external dependencies.

### Expected behavior

When re-exporting from an external module using `export *`, all exports from that module should be accessible through the re-exporting module. The bundler should correctly resolve the external module's namespace and make it available to importers.

### Additional context

This seems to specifically affect re-exports from external modules (not local modules). Direct imports from the external package work fine, but going through a re-export breaks.

---
Repository: /testbed
